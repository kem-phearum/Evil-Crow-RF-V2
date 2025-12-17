// Modern JS for Evil Crow RF V2
'use strict';

const UI = {
    elements: {
        menuToggle: document.getElementById('menuToggle'),
        navLinks: document.getElementById('navLinks'),
        toastContainer: document.getElementById('toast-container'),
        indicators: document.querySelectorAll('.status-value')
    },

    init() {
        this.setupNavigation();
        this.startPolling();
        console.log('Evil Crow RF UI Initialized');
    },

    setupNavigation() {
        if (this.elements.menuToggle) {
            this.elements.menuToggle.addEventListener('click', () => {
                this.elements.navLinks.classList.toggle('show');
                this.elements.menuToggle.textContent =
                    this.elements.navLinks.classList.contains('show') ? '✕' : '☰';
            });
        }

        // Highlight active link
        const currentPath = window.location.pathname;
        document.querySelectorAll('.nav-link').forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
        });
    },

    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.innerHTML = `
      <span>${message}</span>
      <span style="cursor:pointer; margin-left:10px" onclick="this.parentElement.remove()">✕</span>
    `;

        if (!this.elements.toastContainer) {
            console.error("Toast container missing");
            return;
        }

        this.elements.toastContainer.appendChild(toast);

        // Auto remove
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    },

    async startPolling() {
        // Poll on ALL pages to show status alerts
        const poll = async () => {
            try {
                const response = await fetch('/stats');
                if (response.ok) {
                    const data = await response.json();
                    this.updateStats(data);
                    this.updateConnectionStatus(true);
                } else {
                    throw new Error('Network response was not ok');
                }
            } catch (error) {
                this.updateConnectionStatus(false);
            }
            setTimeout(poll, 2000);
        };
        poll();
    },

    updateConnectionStatus(online) {
        const el = document.getElementById('connection-status');
        if (el) {
            el.textContent = online ? 'Online' : 'Offline';
            el.className = `stat-value ${online ? 'ok' : 'err'}`;
        }
    },

    updateStats(data) {
        const set = (id, val) => {
            const el = document.getElementById(id);
            if (el) el.textContent = val;
        };

        set('uptime', this.formatUptime(data.uptime));
        set('cpu0', `${data.cpu0} MHz`);
        set('cpu1', `${data.cpu1} MHz`);
        set('temperature', `${data.temperature?.toFixed(1)} °C`);
        set('totalram', this.formatBytes(data.totalram));
        set('freeram', this.formatBytes(data.freeram));
        set('freespiffs', this.formatBytes(data.freespiffs));
        set('ssid', data.ssid || 'N/A');
        set('ipaddress', data.ipaddress || 'N/A');

        // Storage
        set('sdcard_present', data.sdcard_present ? 'Yes' : 'No');
        set('sdcard_size_gb', `${data.sdcard_size_gb || 0} GB`);
        set('sdcard_free_gb', `${data.sdcard_free_gb || 0} GB`);

        // Handle Status Alerts
        if (data.rx_active || data.tx_active) {
            this.showStatusBanner(data.rx_active, data.tx_active, data.current_freq);
        } else {
            this.hideStatusBanner();
        }
    },

    showStatusBanner(rx, tx, freq) {
        let banner = document.getElementById('status-banner');
        if (!banner) {
            banner = document.createElement('div');
            banner.id = 'status-banner';
            // Insert after header
            const header = document.querySelector('header');
            if (header && header.nextSibling) {
                header.parentNode.insertBefore(banner, header.nextSibling);
            } else {
                document.body.prepend(banner);
            }
        }

        // Update class and text only if changed to avoid flicker
        const newClass = 'status-banner ' + (tx ? 'tx' : 'rx');

        let statusText = tx ? 'TRANSMISSION ACTIVE' : 'RECEIVING SIGNAL...';
        if (freq && parseFloat(freq) > 0) {
            statusText += ` (${parseFloat(freq).toFixed(2)} MHz)`;
        }
        if (tx) statusText = '⚠️ ' + statusText + ' ⚠️';
        else statusText = '● ' + statusText;

        if (banner.className !== newClass) banner.className = newClass;
        if (banner.textContent !== statusText) banner.textContent = statusText;
    },

    hideStatusBanner() {
        const banner = document.getElementById('status-banner');
        if (banner) banner.remove();
    },

    formatBytes(bytes) {
        if (bytes === 0) return '0 B';
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    },

    formatUptime(seconds) {
        if (!seconds) return '--';
        const h = Math.floor(seconds / 3600);
        const m = Math.floor((seconds % 3600) / 60);
        const s = seconds % 60;
        return `${h}h ${m}m ${s}s`;
    }
};

window.showMessage = (type, msg) => UI.showToast(msg, type);

document.addEventListener('DOMContentLoaded', () => UI.init());
