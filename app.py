<!doctype html>
<html lang="id" class="h-full">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIM Perpustakaan</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/_sdk/element_sdk.js"></script>
  <script src="/_sdk/data_sdk.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <style>
    body {
      box-sizing: border-box;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 16px;
      line-height: 1.6;
    }
    .sidebar-item {
      transition: all 0.2s ease;
      font-size: 15px;
    }
    .sidebar-item:hover {
      background: rgba(255,255,255,0.1);
    }
    .sidebar-item.active {
      background: rgba(255,255,255,0.2);
      border-left: 4px solid #fbbf24;
    }
    .card {
      background: white;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .btn-primary {
      background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 15px;
      transition: all 0.2s;
      border: none;
      cursor: pointer;
    }
    .btn-primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(37,99,235,0.4);
    }
    .btn-secondary {
      background: #e2e8f0;
      color: #1e293b;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 15px;
      transition: all 0.2s;
      border: none;
      cursor: pointer;
    }
    .btn-danger {
      background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 15px;
      border: none;
      cursor: pointer;
    }
    .input-field {
      width: 100%;
      padding: 12px 16px;
      border: 2px solid #cbd5e1;
      border-radius: 8px;
      transition: all 0.2s;
      font-size: 15px;
      color: #0f172a;
    }
    .input-field:focus {
      outline: none;
      border-color: #2563eb;
      box-shadow: 0 0 0 3px rgba(37,99,235,0.1);
    }
    .stat-card {
      background: linear-gradient(135deg, var(--stat-color) 0%, var(--stat-color-dark) 100%);
      color: white;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .table-container {
      overflow-x: auto;
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 15px;
    }
    .data-table th {
      background: #f1f5f9;
      padding: 14px 12px;
      text-align: left;
      font-weight: 700;
      color: #0f172a;
      border-bottom: 2px solid #cbd5e1;
      font-size: 15px;
    }
    .data-table td {
      padding: 14px 12px;
      border-bottom: 1px solid #e2e8f0;
      color: #1e293b;
      font-size: 15px;
    }
    .data-table tr:hover {
      background: #f8fafc;
    }
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }
    .modal-content {
      background: white;
      border-radius: 16px;
      max-width: 600px;
      width: 90%;
      max-height: 90%;
      overflow-y: auto;
    }
    .barcode {
      font-family: 'Libre Barcode 39', cursive;
      font-size: 48px;
    }
    .badge {
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
    }
    .badge-success { background: #bbf7d0; color: #14532d; border: 1px solid #86efac; }
    .badge-warning { background: #fde68a; color: #78350f; border: 1px solid #fbbf24; }
    .badge-danger { background: #fecaca; color: #7f1d1d; border: 1px solid #f87171; }
    .badge-info { background: #bfdbfe; color: #1e3a8a; border: 1px solid #60a5fa; }
    @media print {
      .no-print { display: none !important; }
    }
    .toast {
      position: fixed;
      bottom: 20px;
      right: 20px;
      padding: 16px 24px;
      border-radius: 8px;
      color: white;
      font-weight: 500;
      z-index: 2000;
      animation: slideIn 0.3s ease;
    }
    @keyframes slideIn {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    .loading-spinner {
      border: 3px solid #f3f3f3;
      border-top: 3px solid #3b82f6;
      border-radius: 50%;
      width: 24px;
      height: 24px;
      animation: spin 1s linear infinite;
    }
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  </style>
  <style>@view-transition { navigation: auto; }</style>
 </head>
 <body class="h-full bg-gray-100">
  <div id="app" class="h-full"><!-- Login Page -->
   <div id="loginPage" class="h-full flex items-center justify-center" style="background: linear-gradient(135deg, #1e3a5f 0%, #0c1929 100%);">
    <div class="card p-8 w-full max-w-md mx-4">
     <div class="text-center mb-8">
      <div class="w-20 h-20 mx-auto mb-4 bg-gradient-to-br from-blue-500 to-blue-700 rounded-2xl flex items-center justify-center">
       <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
       </svg>
      </div>
      <h1 class="text-2xl font-bold text-gray-800">SIM Perpustakaan</h1>
      <p class="text-gray-500 mt-2">Silakan masuk untuk melanjutkan</p>
     </div>
     <form id="loginForm" onsubmit="handleLogin(event)">
      <div class="mb-4"><label class="block text-sm font-medium text-gray-700 mb-2">Nama Pengguna</label> <input type="text" id="loginName" class="input-field" placeholder="Masukkan nama" required>
      </div>
      <div class="mb-6"><label class="block text-sm font-medium text-gray-700 mb-2">Password</label> <input type="password" id="loginPassword" class="input-field" placeholder="Masukkan password" required>
      </div><button type="submit" class="btn-primary w-full">Masuk</button>
      <p id="loginError" class="text-red-500 text-sm mt-3 text-center hidden">Nama atau password salah</p>
     </form>
    </div>
   </div><!-- Main App -->
   <div id="mainApp" class="h-full flex hidden"><!-- Sidebar -->
    <aside id="sidebar" class="w-64 bg-gradient-to-b from-slate-800 to-slate-900 text-white flex flex-col flex-shrink-0">
     <div class="p-5 border-b border-slate-700">
      <div class="flex items-center gap-3">
       <div id="sidebarLogo" class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-700 rounded-xl flex items-center justify-center">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
        </svg>
       </div>
       <div>
        <h2 id="appTitle" class="font-bold text-lg">Perpustakaan</h2>
        <p id="schoolNameSidebar" class="text-xs text-slate-400">Sistem Informasi</p>
       </div>
      </div>
     </div>
     <nav class="flex-1 py-4 overflow-y-auto">
      <div id="menuItems"></div>
     </nav>
     <div class="p-4 border-t border-slate-700">
      <div class="flex items-center gap-3 mb-3">
       <div id="userAvatar" class="w-10 h-10 bg-slate-600 rounded-full flex items-center justify-center text-sm font-bold">
        U
       </div>
       <div class="flex-1 min-w-0">
        <p id="userName" class="font-medium text-sm truncate">User</p>
        <p id="userRole" class="text-xs text-slate-400">Role</p>
       </div>
      </div><button onclick="handleLogout()" class="w-full py-2 px-3 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition flex items-center justify-center gap-2">
       <svg class="w-4 h-4" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
       </svg> Keluar </button>
     </div>
    </aside><!-- Main Content -->
    <main class="flex-1 flex flex-col overflow-hidden"><!-- Header -->
     <header class="bg-white shadow-sm px-6 py-4 flex items-center justify-between flex-shrink-0">
      <div>
       <h1 id="pageTitle" class="text-2xl font-bold text-gray-900">Dashboard</h1>
       <p id="pageSubtitle" class="text-base text-gray-700">Selamat datang di sistem perpustakaan</p>
      </div>
      <div class="flex items-center gap-4">
       <div id="liveTime" class="text-right">
        <p id="currentDate" class="text-sm font-medium text-gray-800"></p>
        <p id="currentTime" class="text-2xl font-bold text-blue-600"></p>
       </div>
      </div>
     </header><!-- Content Area -->
     <div id="contentArea" class="flex-1 overflow-y-auto p-6"><!-- Dynamic content will be loaded here -->
     </div>
    </main>
   </div><!-- Modal Container -->
   <div id="modalContainer"></div><!-- Toast Container -->
   <div id="toastContainer"></div>
  </div>
  <script>
    // ==================== STATE MANAGEMENT ====================
    let currentUser = null;
    let currentPage = 'dashboard';
    let allData = {
      books: [],
      members: [],
      borrowings: [],
      visits: [],
      income: [],
      expenses: [],
      settings: null,
      pdfs: [],
      music: []
    };
    let isLoading = false;

    const defaultConfig = {
      app_title: 'SIM Perpustakaan',
      primary_color: '#1e3a5f',
      secondary_color: '#3b82f6',
      accent_color: '#fbbf24',
      text_color: '#1f2937',
      background_color: '#f3f4f6'
    };

    let config = { ...defaultConfig };

    // Admin credentials
    const ADMIN_NAME = 'Muhammad Itsna Ali Tiyas Bahari';
    const ADMIN_PASSWORD = 'Ali16052000';

    // Menu items based on role
    const adminMenus = [
      { id: 'dashboard', icon: 'home', label: 'Dashboard' },
      { id: 'books', icon: 'book', label: 'Data Buku' },
      { id: 'members', icon: 'users', label: 'Data Anggota' },
      { id: 'borrowing', icon: 'hand', label: 'Peminjaman' },
      { id: 'return', icon: 'refresh', label: 'Pengembalian' },
      { id: 'visit', icon: 'calendar', label: 'Kunjungan' },
      { id: 'history', icon: 'clock', label: 'Riwayat' },
      { id: 'reports', icon: 'chart', label: 'Laporan' },
      { id: 'finance', icon: 'money', label: 'Keuangan' },
      { id: 'settings', icon: 'cog', label: 'Pengaturan' }
    ];

    const memberMenus = [
      { id: 'dashboard', icon: 'home', label: 'Dashboard' },
      { id: 'books', icon: 'book', label: 'Katalog Buku' },
      { id: 'history', icon: 'clock', label: 'Riwayat Saya' }
    ];

    // ==================== ICONS ====================
    const icons = {
      home: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>',
      book: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>',
      users: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>',
      hand: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 113 0m-3 6a1.5 1.5 0 00-3 0v2a7.5 7.5 0 0015 0v-5a1.5 1.5 0 00-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 013 0v1m0 0V11m0-5.5a1.5 1.5 0 013 0v3m0 0V11"/>',
      refresh: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>',
      calendar: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>',
      clock: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>',
      chart: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>',
      money: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>',
      cog: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>',
      file: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>',
      music: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>',
      plus: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>',
      search: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>',
      print: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/>',
      edit: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>',
      trash: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>',
      download: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>',
      play: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>',
      pause: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"/>'
    };

    function getIcon(name, className = 'w-5 h-5') {
      return `<svg class="${className}" fill="none" stroke="currentColor" viewBox="0 0 24 24">${icons[name] || ''}</svg>`;
    }

    // ==================== UTILITY FUNCTIONS ====================
    function showToast(message, type = 'success') {
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      toast.className = `toast ${type === 'success' ? 'bg-green-500' : type === 'error' ? 'bg-red-500' : 'bg-blue-500'}`;
      toast.textContent = message;
      container.appendChild(toast);
      setTimeout(() => toast.remove(), 3000);
    }

    function formatDate(date) {
      const d = new Date(date);
      return d.toLocaleDateString('id-ID', { day: '2-digit', month: 'long', year: 'numeric' });
    }

    function formatCurrency(amount) {
      return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(amount);
    }

    function generateId() {
      return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }

    function generateBarcode(text) {
      const barcodeChars = '*' + text.toUpperCase() + '*';
      return `<div style="font-family: 'Libre Barcode 39', monospace; font-size: 40px; letter-spacing: 2px;">${barcodeChars}</div><div style="font-size: 12px; text-align: center; margin-top: 4px;">${text}</div>`;
    }

    // Convert Google Drive sharing URL to direct image URL
    function convertGoogleDriveUrl(url) {
      if (!url) return null;
      
      // Extract file ID from various Google Drive URL formats
      let fileId = null;
      
      // Format: https://drive.google.com/file/d/FILE_ID/view
      const match1 = url.match(/\/file\/d\/([a-zA-Z0-9_-]+)/);
      if (match1) fileId = match1[1];
      
      // Format: https://drive.google.com/open?id=FILE_ID
      const match2 = url.match(/[?&]id=([a-zA-Z0-9_-]+)/);
      if (match2) fileId = match2[1];
      
      // Format: https://drive.google.com/uc?id=FILE_ID
      const match3 = url.match(/\/uc\?id=([a-zA-Z0-9_-]+)/);
      if (match3) fileId = match3[1];
      
      if (fileId) {
        // Return direct download URL
        return `https://drive.google.com/uc?export=view&id=${fileId}`;
      }
      
      return url; // Return original URL if no pattern matched
    }

    function isWorkday(date) {
      const day = date.getDay();
      return day !== 0 && day !== 6;
    }

    function getNextWorkday(date) {
      const result = new Date(date);
      while (!isWorkday(result)) {
        result.setDate(result.getDate() + 1);
      }
      return result;
    }

    function calculateDueDate(borrowDate, days = 7) {
      const due = new Date(borrowDate);
      due.setDate(due.getDate() + days);
      return getNextWorkday(due);
    }

    function getDaysOverdue(dueDate) {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const due = new Date(dueDate);
      due.setHours(0, 0, 0, 0);
      const diff = Math.floor((today - due) / (1000 * 60 * 60 * 24));
      return diff > 0 ? diff : 0;
    }

    // ==================== LIVE TIME ====================
    function updateLiveTime() {
      const now = new Date();
      const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
      const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
      
      const dateStr = `${days[now.getDay()]}, ${now.getDate()} ${months[now.getMonth()]} ${now.getFullYear()}`;
      const timeStr = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      
      const dateEl = document.getElementById('currentDate');
      const timeEl = document.getElementById('currentTime');
      if (dateEl) dateEl.textContent = dateStr;
      if (timeEl) timeEl.textContent = timeStr;
    }

    // ==================== DATA HANDLER ====================
    const dataHandler = {
      onDataChanged(data) {
        allData.books = data.filter(d => d.type === 'book');
        allData.members = data.filter(d => d.type === 'member');
        allData.borrowings = data.filter(d => d.type === 'borrowing');
        allData.visits = data.filter(d => d.type === 'visit');
        allData.income = data.filter(d => d.type === 'income');
        allData.expenses = data.filter(d => d.type === 'expense');
        allData.pdfs = data.filter(d => d.type === 'pdf');
        allData.music = data.filter(d => d.type === 'music');
        const settingsData = data.find(d => d.type === 'settings');
        if (settingsData) {
          allData.settings = settingsData;
          applySettings(settingsData);
        }
        if (currentUser) {
          renderCurrentPage();
        }
      }
    };

    function applySettings(settings) {
      if (settings.schoolName) {
        const el = document.getElementById('schoolNameSidebar');
        if (el) el.textContent = settings.schoolName;
      }
      if (settings.background) {
        document.body.style.backgroundImage = `url(${settings.background})`;
        document.body.style.backgroundSize = 'cover';
        document.body.style.backgroundPosition = 'center';
      }
      if (settings.logo) {
        const logoEl = document.getElementById('sidebarLogo');
        if (logoEl) {
          logoEl.innerHTML = `<img src="${settings.logo}" class="w-full h-full object-cover rounded-xl" alt="Logo">`;
        }
      }
    }

    // ==================== AUTHENTICATION ====================
    function handleLogin(e) {
      e.preventDefault();
      const name = document.getElementById('loginName').value.trim();
      const password = document.getElementById('loginPassword').value;
      
      // Check admin
      if (name === ADMIN_NAME && password === ADMIN_PASSWORD) {
        currentUser = { name: ADMIN_NAME, role: 'Administrator', isAdmin: true };
        showMainApp();
        return;
      }
      
      // Check members
      const member = allData.members.find(m => m.name === name && m.password === password);
      if (member) {
        currentUser = { ...member, isAdmin: false };
        showMainApp();
        return;
      }
      
      document.getElementById('loginError').classList.remove('hidden');
    }

    function handleLogout() {
      currentUser = null;
      document.getElementById('mainApp').classList.add('hidden');
      document.getElementById('loginPage').classList.remove('hidden');
      document.getElementById('loginForm').reset();
      document.getElementById('loginError').classList.add('hidden');
    }

    function showMainApp() {
      document.getElementById('loginPage').classList.add('hidden');
      document.getElementById('mainApp').classList.remove('hidden');
      
      document.getElementById('userName').textContent = currentUser.name;
      document.getElementById('userRole').textContent = currentUser.role || currentUser.isAdmin ? 'Administrator' : 'Anggota';
      document.getElementById('userAvatar').textContent = currentUser.name.charAt(0).toUpperCase();
      
      renderMenu();
      navigateTo('dashboard');
    }

    // ==================== NAVIGATION ====================
    function renderMenu() {
      const menus = currentUser.isAdmin ? adminMenus : memberMenus;
      const container = document.getElementById('menuItems');
      container.innerHTML = menus.map(menu => `
        <button onclick="navigateTo('${menu.id}')" id="menu-${menu.id}" 
          class="sidebar-item w-full flex items-center gap-3 px-5 py-3 text-left text-slate-200 hover:text-white ${currentPage === menu.id ? 'active' : ''}">
          ${getIcon(menu.icon)}
          <span>${menu.label}</span>
        </button>
      `).join('');
    }

    function navigateTo(page) {
      currentPage = page;
      renderMenu();
      renderCurrentPage();
    }

    function renderCurrentPage() {
      const content = document.getElementById('contentArea');
      const titles = {
        dashboard: ['Dashboard', 'Ringkasan statistik perpustakaan'],
        books: ['Data Buku', 'Kelola koleksi buku perpustakaan'],
        members: ['Data Anggota', 'Kelola anggota perpustakaan'],
        borrowing: ['Peminjaman Buku', 'Catat peminjaman buku'],
        return: ['Pengembalian Buku', 'Proses pengembalian buku'],
        visit: ['Kunjungan Perpustakaan', 'Catat kunjungan harian'],
        history: ['Riwayat Transaksi', 'Riwayat peminjaman, pengembalian, dan kunjungan'],
        reports: ['Laporan', 'Laporan dan statistik perpustakaan'],
        finance: ['Keuangan', 'Kelola pemasukan dan pengeluaran'],
        settings: ['Pengaturan', 'Konfigurasi sistem perpustakaan']
      };
      
      document.getElementById('pageTitle').textContent = titles[currentPage]?.[0] || 'Halaman';
      document.getElementById('pageSubtitle').textContent = titles[currentPage]?.[1] || '';
      
      switch(currentPage) {
        case 'dashboard': renderDashboard(); break;
        case 'books': renderBooks(); break;
        case 'members': renderMembers(); break;
        case 'borrowing': renderBorrowing(); break;
        case 'return': renderReturn(); break;
        case 'visit': renderVisit(); break;
        case 'history': renderHistory(); break;
        case 'reports': renderReports(); break;
        case 'finance': renderFinance(); break;
        case 'settings': renderSettings(); break;
        default: content.innerHTML = '<p>Halaman tidak ditemukan</p>';
      }
    }

    // ==================== DASHBOARD ====================
    function renderDashboard() {
      const totalBooks = allData.books.reduce((sum, b) => sum + (b.stock || 0), 0);
      const totalMembers = allData.members.length;
      const activeBorrowings = allData.borrowings.filter(b => !b.returned).length;
      const today = new Date().toISOString().split('T')[0];
      const todayVisits = allData.visits.filter(v => v.visitDate === today).length;
      const todayBorrowings = allData.borrowings.filter(b => b.borrowDate.split('T')[0] === today);
      
      const overdueBorrowings = allData.borrowings.filter(b => !b.returned && getDaysOverdue(b.dueDate) > 0);
      
      // Popular books
      const bookBorrowCount = {};
      allData.borrowings.forEach(b => {
        bookBorrowCount[b.bookTitle] = (bookBorrowCount[b.bookTitle] || 0) + 1;
      });
      const popularBooks = Object.entries(bookBorrowCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);
      
      // Chart data - Last 7 days
      const last7Days = [];
      const borrowingsByDate = {};
      const visitsByDate = {};
      
      for (let i = 6; i >= 0; i--) {
        const date = new Date();
        date.setDate(date.getDate() - i);
        const dateStr = date.toISOString().split('T')[0];
        last7Days.push({
          date: dateStr,
          label: date.toLocaleDateString('id-ID', { day: '2-digit', month: 'short' })
        });
        borrowingsByDate[dateStr] = 0;
        visitsByDate[dateStr] = 0;
      }
      
      allData.borrowings.forEach(b => {
        const dateStr = b.borrowDate.split('T')[0];
        if (borrowingsByDate[dateStr] !== undefined) {
          borrowingsByDate[dateStr]++;
        }
      });
      
      allData.visits.forEach(v => {
        if (visitsByDate[v.visitDate] !== undefined) {
          visitsByDate[v.visitDate]++;
        }
      });

      const content = document.getElementById('contentArea');
      content.innerHTML = `
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div class="stat-card" style="--stat-color: #3b82f6; --stat-color-dark: #1d4ed8;">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-blue-100 text-sm">Total Buku</p>
                <p class="text-3xl font-bold mt-1">${totalBooks}</p>
              </div>
              ${getIcon('book', 'w-12 h-12 text-blue-200')}
            </div>
          </div>
          <div class="stat-card" style="--stat-color: #10b981; --stat-color-dark: #059669;">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-green-100 text-sm">Total Anggota</p>
                <p class="text-3xl font-bold mt-1">${totalMembers}</p>
              </div>
              ${getIcon('users', 'w-12 h-12 text-green-200')}
            </div>
          </div>
          <div class="stat-card" style="--stat-color: #f59e0b; --stat-color-dark: #d97706;">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-yellow-100 text-sm">Sedang Dipinjam</p>
                <p class="text-3xl font-bold mt-1">${activeBorrowings}</p>
              </div>
              ${getIcon('hand', 'w-12 h-12 text-yellow-200')}
            </div>
          </div>
          <div class="stat-card" style="--stat-color: #8b5cf6; --stat-color-dark: #7c3aed;">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-purple-100 text-sm">Kunjungan Hari Ini</p>
                <p class="text-3xl font-bold mt-1">${todayVisits}</p>
              </div>
              ${getIcon('calendar', 'w-12 h-12 text-purple-200')}
            </div>
          </div>
        </div>

        <div class="card p-6 mb-6">
          <h3 class="text-lg font-bold text-gray-800 mb-4">Statistik Aktivitas 7 Hari Terakhir</h3>
          <div class="h-64 flex items-end justify-between gap-2">
            ${last7Days.map(day => {
              const borrowings = borrowingsByDate[day.date];
              const visits = visitsByDate[day.date];
              const maxValue = Math.max(...Object.values(borrowingsByDate), ...Object.values(visitsByDate), 1);
              const borrowHeight = (borrowings / maxValue) * 100;
              const visitHeight = (visits / maxValue) * 100;
              
              return `
                <div class="flex-1 flex flex-col items-center gap-2">
                  <div class="w-full flex gap-1 items-end justify-center" style="height: 200px;">
                    <div class="relative group flex-1" style="height: ${borrowHeight}%;">
                      <div class="w-full h-full bg-gradient-to-t from-blue-500 to-blue-400 rounded-t hover:from-blue-600 hover:to-blue-500 transition cursor-pointer"></div>
                      <div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-gray-800 text-white text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition whitespace-nowrap">
                        ${borrowings} Peminjaman
                      </div>
                    </div>
                    <div class="relative group flex-1" style="height: ${visitHeight}%;">
                      <div class="w-full h-full bg-gradient-to-t from-purple-500 to-purple-400 rounded-t hover:from-purple-600 hover:to-purple-500 transition cursor-pointer"></div>
                      <div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-gray-800 text-white text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition whitespace-nowrap">
                        ${visits} Kunjungan
                      </div>
                    </div>
                  </div>
                  <span class="text-xs text-gray-600 font-medium">${day.label}</span>
                </div>
              `;
            }).join('')}
          </div>
          <div class="flex justify-center gap-6 mt-4">
            <div class="flex items-center gap-2">
              <div class="w-4 h-4 bg-blue-500 rounded"></div>
              <span class="text-sm text-gray-600">Peminjaman</span>
            </div>
            <div class="flex items-center gap-2">
              <div class="w-4 h-4 bg-purple-500 rounded"></div>
              <span class="text-sm text-gray-600">Kunjungan</span>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
              ${getIcon('clock', 'w-5 h-5 text-red-500')}
              Peminjaman Terlambat (${overdueBorrowings.length})
            </h3>
            ${overdueBorrowings.length === 0 ? 
              '<p class="text-gray-500 text-center py-4">Tidak ada peminjaman terlambat</p>' :
              `<div class="space-y-3 max-h-64 overflow-y-auto">
                ${overdueBorrowings.slice(0, 10).map(b => `
                  <div class="flex items-center justify-between p-3 bg-red-50 rounded-lg">
                    <div>
                      <p class="font-medium text-gray-800">${b.bookTitle}</p>
                      <p class="text-sm text-gray-500">${b.memberName || 'Anggota'}</p>
                    </div>
                    <span class="badge badge-danger">${getDaysOverdue(b.dueDate)} hari</span>
                  </div>
                `).join('')}
              </div>`
            }
          </div>

          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
              ${getIcon('hand', 'w-5 h-5 text-green-500')}
              Peminjaman Hari Ini (${todayBorrowings.length})
            </h3>
            ${todayBorrowings.length === 0 ? 
              '<p class="text-gray-500 text-center py-4">Belum ada peminjaman hari ini</p>' :
              `<div class="space-y-3 max-h-64 overflow-y-auto">
                ${todayBorrowings.map(b => `
                  <div class="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                    <div>
                      <p class="font-medium text-gray-800">${b.bookTitle}</p>
                      <p class="text-sm text-gray-500">${b.memberName || 'Anggota'}</p>
                    </div>
                    <span class="badge badge-success">Hari ini</span>
                  </div>
                `).join('')}
              </div>`
            }
          </div>

          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
              ${getIcon('chart', 'w-5 h-5 text-blue-500')}
              Buku Terpopuler
            </h3>
            ${popularBooks.length === 0 ? 
              '<p class="text-gray-500 text-center py-4">Belum ada data peminjaman</p>' :
              `<div class="space-y-3">
                ${popularBooks.map((b, i) => `
                  <div class="flex items-center gap-3">
                    <span class="w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold text-sm">${i + 1}</span>
                    <div class="flex-1">
                      <p class="font-medium text-gray-800">${b[0]}</p>
                      <p class="text-sm text-gray-500">${b[1]} kali dipinjam</p>
                    </div>
                  </div>
                `).join('')}
              </div>`
            }
          </div>
        </div>
      `;
    }

    // ==================== BOOKS ====================
    function renderBooks() {
      const content = document.getElementById('contentArea');
      const isAdmin = currentUser.isAdmin;
      
      content.innerHTML = `
        <div class="card p-6 mb-6">
          <div class="flex flex-wrap gap-4 items-center justify-between mb-6">
            <div class="flex-1 min-w-64">
              <div class="relative">
                <input type="text" id="bookSearch" placeholder="Cari buku..." class="input-field pl-10" oninput="filterBooks()">
                <div class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">${getIcon('search', 'w-5 h-5')}</div>
              </div>
            </div>
            ${isAdmin ? `<button onclick="showBookModal()" class="btn-primary flex items-center gap-2">${getIcon('plus', 'w-5 h-5')} Tambah Buku</button>` : ''}
          </div>
          
          <div class="table-container">
            <table class="data-table" id="booksTable">
              <thead>
                <tr>
                  <th>ISBN</th>
                  <th>Judul</th>
                  <th>Penulis</th>
                  <th>Kategori</th>
                  <th>Stok</th>
                  <th>Tersedia</th>
                  <th>Rak</th>
                  ${isAdmin ? '<th>Aksi</th>' : ''}
                </tr>
              </thead>
              <tbody id="booksTableBody">
                ${renderBooksRows(allData.books)}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function renderBooksRows(books) {
      const isAdmin = currentUser.isAdmin;
      if (books.length === 0) {
        return `<tr><td colspan="${isAdmin ? 8 : 7}" class="text-center py-8 text-gray-500">Belum ada data buku</td></tr>`;
      }
      return books.map(book => `
        <tr data-id="${book.__backendId}">
          <td><code class="bg-gray-100 px-2 py-1 rounded text-sm">${book.isbn || '-'}</code></td>
          <td class="font-medium">${book.title}</td>
          <td>${book.author || '-'}</td>
          <td><span class="badge badge-info">${book.category || '-'}</span></td>
          <td>${book.stock || 0}</td>
          <td><span class="badge ${(book.available || 0) > 0 ? 'badge-success' : 'badge-danger'}">${book.available || 0}</span></td>
          <td>${book.location || '-'}</td>
          ${isAdmin ? `
            <td>
              <div class="flex gap-2">
                <button onclick="showBookModal('${book.__backendId}')" class="p-2 hover:bg-gray-100 rounded-lg" title="Edit">${getIcon('edit', 'w-4 h-4 text-blue-600')}</button>
                <button onclick="printBookBarcode('${book.__backendId}')" class="p-2 hover:bg-gray-100 rounded-lg" title="Cetak Barcode">${getIcon('print', 'w-4 h-4 text-green-600')}</button>
                <button onclick="confirmDelete('book', '${book.__backendId}')" class="p-2 hover:bg-gray-100 rounded-lg" title="Hapus">${getIcon('trash', 'w-4 h-4 text-red-600')}</button>
              </div>
            </td>
          ` : ''}
        </tr>
      `).join('');
    }

    function filterBooks() {
      const search = document.getElementById('bookSearch').value.toLowerCase();
      const filtered = allData.books.filter(b => 
        (b.title || '').toLowerCase().includes(search) ||
        (b.author || '').toLowerCase().includes(search) ||
        (b.isbn || '').toLowerCase().includes(search) ||
        (b.category || '').toLowerCase().includes(search)
      );
      document.getElementById('booksTableBody').innerHTML = renderBooksRows(filtered);
    }

    function showBookModal(bookId = null) {
      const book = bookId ? allData.books.find(b => b.__backendId === bookId) : null;
      const isEdit = !!book;
      
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'bookModal';
      modal.innerHTML = `
        <div class="modal-content p-6">
          <h2 class="text-xl font-bold mb-6">${isEdit ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
          <form id="bookForm" onsubmit="saveBook(event, ${isEdit ? `'${bookId}'` : 'null'})">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">ISBN</label>
                <input type="text" name="isbn" class="input-field" value="${book?.isbn || ''}" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Judul Buku</label>
                <input type="text" name="title" class="input-field" value="${book?.title || ''}" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Kategori</label>
                <select name="category" class="input-field" required>
                  <option value="">Pilih Kategori</option>
                  <option ${book?.category === 'Fiksi' ? 'selected' : ''}>Fiksi</option>
                  <option ${book?.category === 'Non-Fiksi' ? 'selected' : ''}>Non-Fiksi</option>
                  <option ${book?.category === 'Pendidikan' ? 'selected' : ''}>Pendidikan</option>
                  <option ${book?.category === 'Sains' ? 'selected' : ''}>Sains</option>
                  <option ${book?.category === 'Teknologi' ? 'selected' : ''}>Teknologi</option>
                  <option ${book?.category === 'Sejarah' ? 'selected' : ''}>Sejarah</option>
                  <option ${book?.category === 'Agama' ? 'selected' : ''}>Agama</option>
                  <option ${book?.category === 'Bahasa' ? 'selected' : ''}>Bahasa</option>
                  <option ${book?.category === 'Referensi' ? 'selected' : ''}>Referensi</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Penulis</label>
                <input type="text" name="author" class="input-field" value="${book?.author || ''}" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Penerbit</label>
                <input type="text" name="publisher" class="input-field" value="${book?.publisher || ''}">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Tahun Terbit</label>
                <input type="number" name="year" class="input-field" value="${book?.year || ''}" min="1900" max="2099">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Jumlah Stok</label>
                <input type="number" name="stock" class="input-field" value="${book?.stock || 1}" min="1" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Lokasi Rak</label>
                <input type="text" name="location" class="input-field" value="${book?.location || ''}" placeholder="Contoh: A-01">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Foto Buku</label>
                <div class="space-y-2">
                  <input type="file" accept="image/jpeg,image/jpg,image/png" onchange="previewBookPhoto(event)" class="input-field">
                  <input type="hidden" name="bookPhoto" id="bookPhotoData" value="${book?.bookPhoto || ''}">
                  ${book?.bookPhoto ? `<img src="${book.bookPhoto}" class="mt-2 w-24 h-32 object-cover rounded-lg border-2 border-gray-200">` : ''}
                  <div id="bookPhotoPreview" class="mt-2"></div>
                  <p class="text-xs text-gray-500">Upload file JPG/PNG</p>
                </div>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button type="submit" class="btn-primary flex-1">Simpan</button>
              <button type="button" onclick="closeModal('bookModal')" class="btn-secondary">Batal</button>
            </div>
          </form>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    function previewBookPhoto(e) {
      const file = e.target.files[0];
      if (!file) return;
      
      const reader = new FileReader();
      reader.onload = function(event) {
        const base64 = event.target.result;
        document.getElementById('bookPhotoData').value = base64;
        document.getElementById('bookPhotoPreview').innerHTML = `<img src="${base64}" class="w-24 h-32 object-cover rounded-lg border-2 border-gray-200">`;
      };
      reader.readAsDataURL(file);
    }

    function previewMemberPhoto(e) {
      const file = e.target.files[0];
      if (!file) return;
      
      const reader = new FileReader();
      reader.onload = function(event) {
        const base64 = event.target.result;
        document.getElementById('memberPhotoData').value = base64;
        document.getElementById('memberPhotoPreview').innerHTML = `<img src="${base64}" class="w-24 h-24 object-cover rounded-full border-2 border-gray-200">`;
      };
      reader.readAsDataURL(file);
    }

    function previewMusic(e) {
      const file = e.target.files[0];
      if (!file) return;
      
      // Check file size (max 10MB)
      if (file.size > 10 * 1024 * 1024) {
        showToast('Ukuran file maksimal 10MB', 'error');
        e.target.value = '';
        return;
      }
      
      const reader = new FileReader();
      reader.onload = function(event) {
        const base64 = event.target.result;
        document.getElementById('musicDataBase64').value = base64;
        document.getElementById('musicPreview').innerHTML = `
          <div class="flex items-center gap-3 p-3 bg-green-50 rounded-lg">
            <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
              ${getIcon('music', 'w-5 h-5 text-green-600')}
            </div>
            <div class="flex-1">
              <p class="text-sm font-medium text-gray-800">${file.name}</p>
              <p class="text-xs text-gray-500">${(file.size / 1024 / 1024).toFixed(2)} MB</p>
            </div>
            <span class="text-green-600 text-xs">✓ Siap diupload</span>
          </div>
        `;
      };
      reader.readAsDataURL(file);
    }



    async function saveBook(e, bookId) {
      e.preventDefault();
      
      // Show loading state
      const submitBtn = e.target.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<div class="loading-spinner mx-auto"></div>';
      
      try {
        const form = e.target;
        const formData = new FormData(form);
        
        const bookData = {
          type: 'book',
          isbn: formData.get('isbn'),
          title: formData.get('title'),
          category: formData.get('category'),
          author: formData.get('author'),
          publisher: formData.get('publisher'),
          year: formData.get('year'),
          stock: parseInt(formData.get('stock')) || 1,
          available: parseInt(formData.get('stock')) || 1,
          location: formData.get('location'),
          bookPhoto: document.getElementById('bookPhotoData').value || ''
        };
        
        if (bookId) {
          const existingBook = allData.books.find(b => b.__backendId === bookId);
          if (existingBook) {
            const borrowedCount = (existingBook.stock || 0) - (existingBook.available || 0);
            bookData.available = Math.max(0, bookData.stock - borrowedCount);
            const result = await window.dataSdk.update({ ...existingBook, ...bookData });
            if (result.isOk) {
              showToast('Buku berhasil diperbarui');
              closeModal('bookModal');
            } else {
              showToast('Gagal memperbarui buku', 'error');
              submitBtn.disabled = false;
              submitBtn.textContent = originalText;
            }
          }
        } else {
          if (allData.books.length >= 999) {
            showToast('Batas maksimal 999 data tercapai', 'error');
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
            return;
          }
          const result = await window.dataSdk.create(bookData);
          if (result.isOk) {
            showToast('Buku berhasil ditambahkan');
            closeModal('bookModal');
          } else {
            showToast('Gagal menambahkan buku', 'error');
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
          }
        }
      } catch (error) {
        showToast('Terjadi kesalahan: ' + error.message, 'error');
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    }

    function printBookBarcode(bookId) {
      const book = allData.books.find(b => b.__backendId === bookId);
      if (!book) return;
      
      const quantity = parseInt(prompt('Cetak berapa barcode?', book.stock || 1)) || 1;
      const barcodes = [];
      for (let i = 0; i < quantity; i++) {
        barcodes.push(`
          <div style="display: inline-block; margin: 10px; padding: 15px; border: 1px solid #ccc; text-align: center;">
            ${generateBarcode(book.isbn || book.__backendId)}
            <div style="font-size: 10px; margin-top: 5px;">${book.title}</div>
          </div>
        `);
      }
      
      const printWindow = window.open('', '_blank');
      printWindow.document.write(`
        <html>
          <head>
            <title>Cetak Barcode - ${book.title}</title>
            <link href="https://fonts.googleapis.com/css2?family=Libre+Barcode+39&display=swap" rel="stylesheet">
            <style>body { font-family: Arial, sans-serif; }</style>
          </head>
          <body>${barcodes.join('')}</body>
        </html>
      `);
      printWindow.document.close();
      printWindow.print();
    }

    // ==================== MEMBERS ====================
    function renderMembers() {
      const content = document.getElementById('contentArea');
      
      content.innerHTML = `
        <div class="card p-6 mb-6">
          <div class="flex flex-wrap gap-4 items-center justify-between mb-6">
            <div class="flex-1 min-w-64">
              <div class="relative">
                <input type="text" id="memberSearch" placeholder="Cari anggota..." class="input-field pl-10" oninput="filterMembers()">
                <div class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">${getIcon('search', 'w-5 h-5')}</div>
              </div>
            </div>
            <button onclick="showMemberModal()" class="btn-primary flex items-center gap-2">${getIcon('plus', 'w-5 h-5')} Tambah Anggota</button>
          </div>
          
          <div class="table-container">
            <table class="data-table" id="membersTable">
              <thead>
                <tr>
                  <th>Foto</th>
                  <th>NIS/NIP</th>
                  <th>Nama</th>
                  <th>Role</th>
                  <th>Kelas</th>
                  <th>Status</th>
                  <th>Telepon</th>
                  <th>Aksi</th>
                </tr>
              </thead>
              <tbody id="membersTableBody">
                ${renderMembersRows(allData.members)}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function renderMembersRows(members) {
      if (members.length === 0) {
        return `<tr><td colspan="8" class="text-center py-8 text-gray-500">Belum ada data anggota</td></tr>`;
      }
      return members.map(member => `
        <tr data-id="${member.__backendId}">
          <td>
            <div class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center overflow-hidden">
              ${member.photo ? `<img src="${member.photo}" class="w-full h-full object-cover">` : `<span class="text-gray-500 font-bold">${(member.name || 'A').charAt(0)}</span>`}
            </div>
          </td>
          <td><code class="bg-gray-100 px-2 py-1 rounded text-sm">${member.nis || '-'}</code></td>
          <td class="font-medium">${member.name}</td>
          <td><span class="badge badge-info">${member.role || 'Siswa'}</span></td>
          <td>${member.class || '-'}</td>
          <td><span class="badge ${member.status === 'Aktif' ? 'badge-success' : 'badge-danger'}">${member.status || 'Aktif'}</span></td>
          <td>${member.phone || '-'}</td>
          <td>
            <div class="flex gap-2">
              <button onclick="showMemberModal('${member.__backendId}')" class="p-2 hover:bg-gray-100 rounded-lg" title="Edit">${getIcon('edit', 'w-4 h-4 text-blue-600')}</button>
              <button onclick="printMemberCard('${member.__backendId}')" class="p-2 hover:bg-gray-100 rounded-lg" title="Cetak Kartu">${getIcon('print', 'w-4 h-4 text-green-600')}</button>
              <button onclick="confirmDelete('member', '${member.__backendId}')" class="p-2 hover:bg-gray-100 rounded-lg" title="Hapus">${getIcon('trash', 'w-4 h-4 text-red-600')}</button>
            </div>
          </td>
        </tr>
      `).join('');
    }

    function filterMembers() {
      const search = document.getElementById('memberSearch').value.toLowerCase();
      const filtered = allData.members.filter(m => 
        (m.name || '').toLowerCase().includes(search) ||
        (m.nis || '').toLowerCase().includes(search) ||
        (m.class || '').toLowerCase().includes(search)
      );
      document.getElementById('membersTableBody').innerHTML = renderMembersRows(filtered);
    }

    function showMemberModal(memberId = null) {
      const member = memberId ? allData.members.find(m => m.__backendId === memberId) : null;
      const isEdit = !!member;
      
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'memberModal';
      modal.innerHTML = `
        <div class="modal-content p-6">
          <h2 class="text-xl font-bold mb-6">${isEdit ? 'Edit Anggota' : 'Tambah Anggota Baru'}</h2>
          <form id="memberForm" onsubmit="saveMember(event, ${isEdit ? `'${memberId}'` : 'null'})">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Nama Lengkap</label>
                <input type="text" name="name" class="input-field" value="${member?.name || ''}" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Role</label>
                <select name="role" class="input-field" required>
                  <option value="Siswa" ${member?.role === 'Siswa' ? 'selected' : ''}>Siswa</option>
                  <option value="Guru" ${member?.role === 'Guru' ? 'selected' : ''}>Guru</option>
                  <option value="Staff" ${member?.role === 'Staff' ? 'selected' : ''}>Staff</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
                <select name="status" class="input-field" required>
                  <option value="Aktif" ${member?.status === 'Aktif' || !member ? 'selected' : ''}>Aktif</option>
                  <option value="Tidak Aktif" ${member?.status === 'Tidak Aktif' ? 'selected' : ''}>Tidak Aktif</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">NIS/NIP</label>
                <input type="text" name="nis" class="input-field" value="${member?.nis || ''}" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Kelas</label>
                <input type="text" name="class" class="input-field" value="${member?.class || ''}" placeholder="Contoh: X IPA 1">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">No. Telepon</label>
                <input type="tel" name="phone" class="input-field" value="${member?.phone || ''}">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                <input type="email" name="email" class="input-field" value="${member?.email || ''}">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Alamat</label>
                <textarea name="address" class="input-field" rows="2">${member?.address || ''}</textarea>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Password</label>
                <input type="password" name="password" class="input-field" value="${member?.password || ''}" ${isEdit ? '' : 'required'} placeholder="${isEdit ? 'Kosongkan jika tidak diubah' : ''}">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Foto Anggota</label>
                <div class="space-y-2">
                  <input type="file" accept="image/jpeg,image/jpg,image/png" onchange="previewMemberPhoto(event)" class="input-field">
                  <input type="hidden" name="photo" id="memberPhotoData" value="${member?.photo || ''}">
                  ${member?.photo ? `<img src="${member.photo}" class="mt-2 w-24 h-24 object-cover rounded-full border-2 border-gray-200">` : ''}
                  <div id="memberPhotoPreview" class="mt-2"></div>
                  <p class="text-xs text-gray-500">Upload file JPG/PNG</p>
                </div>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button type="submit" class="btn-primary flex-1">Simpan</button>
              <button type="button" onclick="closeModal('memberModal')" class="btn-secondary">Batal</button>
            </div>
          </form>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    async function saveMember(e, memberId) {
      e.preventDefault();
      
      // Show loading state
      const submitBtn = e.target.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<div class="loading-spinner mx-auto"></div>';
      
      try {
        const form = e.target;
        const formData = new FormData(form);
        
        const memberData = {
          type: 'member',
          name: formData.get('name'),
          role: formData.get('role'),
          status: formData.get('status'),
          nis: formData.get('nis'),
          class: formData.get('class'),
          phone: formData.get('phone'),
          email: formData.get('email'),
          address: formData.get('address'),
          photo: document.getElementById('memberPhotoData').value || ''
        };
        
        const password = formData.get('password');
        if (password) {
          memberData.password = password;
        }
        
        if (memberId) {
          const existingMember = allData.members.find(m => m.__backendId === memberId);
          if (existingMember) {
            if (!password) memberData.password = existingMember.password;
            const result = await window.dataSdk.update({ ...existingMember, ...memberData });
            if (result.isOk) {
              showToast('Anggota berhasil diperbarui');
              closeModal('memberModal');
            } else {
              showToast('Gagal memperbarui anggota', 'error');
              submitBtn.disabled = false;
              submitBtn.textContent = originalText;
            }
          }
        } else {
          if (allData.members.length >= 999) {
            showToast('Batas maksimal 999 data tercapai', 'error');
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
            return;
          }
          const result = await window.dataSdk.create(memberData);
          if (result.isOk) {
            showToast('Anggota berhasil ditambahkan');
            closeModal('memberModal');
          } else {
            showToast('Gagal menambahkan anggota', 'error');
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
          }
        }
      } catch (error) {
        showToast('Terjadi kesalahan: ' + error.message, 'error');
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    }

    function printMemberCard(memberId) {
      const member = allData.members.find(m => m.__backendId === memberId);
      if (!member) return;
      
      const settings = allData.settings || {};
      const printWindow = window.open('', '_blank');
      printWindow.document.write(`
        <html>
          <head>
            <title>Kartu Anggota - ${member.name}</title>
            <link href="https://fonts.googleapis.com/css2?family=Libre+Barcode+39&display=swap" rel="stylesheet">
            <style>
              body { font-family: Arial, sans-serif; }
              .card { width: 350px; height: 200px; border: 2px solid #1e3a5f; border-radius: 12px; padding: 15px; position: relative; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }
              .header { display: flex; align-items: center; gap: 10px; margin-bottom: 15px; border-bottom: 2px solid #1e3a5f; padding-bottom: 10px; }
              .logo { width: 40px; height: 40px; background: #1e3a5f; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; }
              .school-name { font-weight: bold; color: #1e3a5f; }
              .content { display: flex; gap: 15px; }
              .photo { width: 60px; height: 80px; background: #ddd; border-radius: 4px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
              .photo img { width: 100%; height: 100%; object-fit: cover; }
              .info { flex: 1; font-size: 11px; }
              .info p { margin: 3px 0; }
              .barcode-section { position: absolute; bottom: 10px; right: 15px; text-align: right; }
            </style>
          </head>
          <body>
            <div class="card">
              <div class="header">
                <div class="logo">${settings.logo ? `<img src="${settings.logo}" style="width:100%;height:100%;object-fit:cover;border-radius:8px">` : 'P'}</div>
                <div>
                  <div class="school-name">${settings.schoolName || 'Perpustakaan'}</div>
                  <div style="font-size: 10px; color: #666;">Kartu Anggota</div>
                </div>
              </div>
              <div class="content">
                <div class="photo">${member.photo ? `<img src="${member.photo}">` : member.name.charAt(0)}</div>
                <div class="info">
                  <p><strong>${member.name}</strong></p>
                  <p>NIS/NIP: ${member.nis || '-'}</p>
                  <p>Kelas: ${member.class || '-'}</p>
                  <p>Role: ${member.role || 'Siswa'}</p>
                </div>
              </div>
              <div class="barcode-section">
                ${generateBarcode(member.nis || member.__backendId)}
              </div>
            </div>
          </body>
        </html>
      `);
      printWindow.document.close();
      printWindow.print();
    }

    // ==================== BORROWING ====================
    function renderBorrowing() {
      const content = document.getElementById('contentArea');
      const activeBorrowings = allData.borrowings.filter(b => !b.returned);
      
      content.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Form Peminjaman</h3>
            <form id="borrowingForm" onsubmit="processBorrowing(event)">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">ID Anggota / NIS / NIP</label>
                  <div class="flex gap-2">
                    <input type="text" id="borrowMemberId" class="input-field" placeholder="Scan barcode atau ketik dan tekan Enter" required onkeypress="handleMemberKeyPress(event)">
                    <button type="button" onclick="searchMember()" class="btn-secondary">${getIcon('search', 'w-5 h-5')}</button>
                  </div>
                  <p id="memberInfo" class="text-sm text-gray-500 mt-1"></p>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">ISBN / Judul Buku</label>
                  <div class="flex gap-2">
                    <input type="text" id="borrowBookSearch" class="input-field" placeholder="Scan barcode ISBN atau ketik dan tekan Enter" onkeypress="handleBookKeyPress(event)" oninput="searchBooks()">
                  </div>
                  <div id="bookSearchResults" class="mt-2 max-h-40 overflow-y-auto"></div>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Buku Dipilih</label>
                  <div id="selectedBook" class="p-3 bg-gray-50 rounded-lg text-gray-500">Belum ada buku dipilih</div>
                  <input type="hidden" id="selectedBookId">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Tanggal Jatuh Tempo</label>
                  <input type="date" id="dueDate" class="input-field" required>
                </div>
              </div>
              <button type="submit" class="btn-primary w-full mt-6">Proses Peminjaman</button>
            </form>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Peminjaman Aktif (${activeBorrowings.length})</h3>
            <div class="space-y-3 max-h-96 overflow-y-auto">
              ${activeBorrowings.length === 0 ? 
                '<p class="text-gray-500 text-center py-4">Tidak ada peminjaman aktif</p>' :
                activeBorrowings.map(b => {
                  const overdue = getDaysOverdue(b.dueDate);
                  return `
                    <div class="p-4 rounded-lg ${overdue > 0 ? 'bg-red-50 border border-red-200' : 'bg-gray-50'}">
                      <div class="flex justify-between items-start">
                        <div>
                          <p class="font-medium text-gray-800">${b.bookTitle}</p>
                          <p class="text-sm text-gray-500">${b.memberName || 'Anggota'} (${b.memberId})</p>
                          <p class="text-xs text-gray-400 mt-1">Jatuh tempo: ${formatDate(b.dueDate)}</p>
                        </div>
                        ${overdue > 0 ? `<span class="badge badge-danger">${overdue} hari terlambat</span>` : '<span class="badge badge-success">Aktif</span>'}
                      </div>
                    </div>
                  `;
                }).join('')
              }
            </div>
          </div>
        </div>
      `;
      
      // Set default due date
      const defaultDue = calculateDueDate(new Date());
      document.getElementById('dueDate').value = defaultDue.toISOString().split('T')[0];
    }

    function handleMemberKeyPress(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        searchMember();
      }
    }

    function handleBookKeyPress(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        const search = document.getElementById('borrowBookSearch').value.toLowerCase().trim();
        
        if (search.length < 2) {
          showToast('Masukkan minimal 2 karakter untuk mencari', 'error');
          return;
        }
        
        // Search for exact ISBN match first (for barcode scanning)
        const exactIsbnMatch = allData.books.find(b => 
          (b.isbn || '').toLowerCase() === search && (b.available || 0) > 0
        );
        
        if (exactIsbnMatch) {
          // Auto-select the book if exact ISBN match
          selectBook(exactIsbnMatch.__backendId);
          document.getElementById('borrowBookSearch').value = '';
          document.getElementById('bookSearchResults').innerHTML = '';
          showToast('Buku dipilih: ' + exactIsbnMatch.title, 'info');
          // Focus on due date field
          document.getElementById('dueDate').focus();
          return;
        }
        
        // Otherwise show search results
        searchBooks();
        
        // If only one result, auto-select it
        const results = allData.books.filter(b => 
          ((b.title || '').toLowerCase().includes(search) || (b.isbn || '').toLowerCase().includes(search)) &&
          (b.available || 0) > 0
        );
        
        if (results.length === 1) {
          selectBook(results[0].__backendId);
          document.getElementById('borrowBookSearch').value = '';
          document.getElementById('bookSearchResults').innerHTML = '';
          showToast('Buku dipilih: ' + results[0].title, 'info');
          // Focus on due date field
          document.getElementById('dueDate').focus();
        } else if (results.length === 0) {
          showToast('Buku tidak ditemukan atau tidak tersedia', 'error');
        }
      }
    }

    function searchMember() {
      const id = document.getElementById('borrowMemberId').value.trim();
      const member = allData.members.find(m => m.nis === id || m.__backendId === id || m.name.toLowerCase().includes(id.toLowerCase()));
      const infoEl = document.getElementById('memberInfo');
      
      if (member) {
        infoEl.innerHTML = `<span class="text-green-600">✓ ${member.name} (${member.role || 'Siswa'})</span>`;
        document.getElementById('borrowMemberId').dataset.memberId = member.__backendId;
        document.getElementById('borrowMemberId').dataset.memberName = member.name;
      } else {
        infoEl.innerHTML = `<span class="text-red-500">✗ Anggota tidak ditemukan</span>`;
      }
    }

    function searchBooks() {
      const search = document.getElementById('borrowBookSearch').value.toLowerCase();
      const resultsEl = document.getElementById('bookSearchResults');
      
      if (search.length < 2) {
        resultsEl.innerHTML = '';
        return;
      }
      
      const results = allData.books.filter(b => 
        ((b.title || '').toLowerCase().includes(search) || (b.isbn || '').toLowerCase().includes(search)) &&
        (b.available || 0) > 0
      ).slice(0, 5);
      
      resultsEl.innerHTML = results.length === 0 ? 
        '<p class="text-sm text-gray-500 p-2">Tidak ada buku yang tersedia</p>' :
        results.map(b => `
          <button type="button" onclick="selectBook('${b.__backendId}')" class="w-full p-2 text-left hover:bg-blue-50 rounded border-b">
            <span class="font-medium">${b.title}</span>
            <span class="text-sm text-gray-500 block">${b.isbn || '-'} • Tersedia: ${b.available}</span>
          </button>
        `).join('');
    }

    function selectBook(bookId) {
      const book = allData.books.find(b => b.__backendId === bookId);
      if (book) {
        document.getElementById('selectedBook').innerHTML = `
          <span class="font-medium">${book.title}</span>
          <span class="text-sm text-gray-500 block">ISBN: ${book.isbn || '-'} • Rak: ${book.location || '-'}</span>
        `;
        document.getElementById('selectedBookId').value = bookId;
        document.getElementById('bookSearchResults').innerHTML = '';
        document.getElementById('borrowBookSearch').value = '';
      }
    }

    async function processBorrowing(e) {
      e.preventDefault();
      
      const memberInput = document.getElementById('borrowMemberId');
      const memberId = memberInput.dataset.memberId;
      const memberName = memberInput.dataset.memberName;
      const bookId = document.getElementById('selectedBookId').value;
      const dueDate = document.getElementById('dueDate').value;
      
      if (!memberId) {
        showToast('Silakan cari dan pilih anggota terlebih dahulu', 'error');
        return;
      }
      
      if (!bookId) {
        showToast('Silakan pilih buku terlebih dahulu', 'error');
        return;
      }
      
      const book = allData.books.find(b => b.__backendId === bookId);
      if (!book || (book.available || 0) < 1) {
        showToast('Buku tidak tersedia', 'error');
        return;
      }
      
      // Create borrowing record
      const borrowingData = {
        type: 'borrowing',
        memberId: memberId,
        memberName: memberName,
        bookId: bookId,
        bookTitle: book.title,
        bookIsbn: book.isbn,
        borrowDate: new Date().toISOString(),
        dueDate: dueDate,
        returned: false,
        returnDate: null,
        fine: 0
      };
      
      const result = await window.dataSdk.create(borrowingData);
      if (result.isOk) {
        // Update book availability
        await window.dataSdk.update({ ...book, available: (book.available || 1) - 1 });
        showToast('Peminjaman berhasil dicatat');
        e.target.reset();
        document.getElementById('memberInfo').innerHTML = '';
        document.getElementById('selectedBook').innerHTML = 'Belum ada buku dipilih';
        document.getElementById('selectedBookId').value = '';
        delete memberInput.dataset.memberId;
        delete memberInput.dataset.memberName;
        const defaultDue = calculateDueDate(new Date());
        document.getElementById('dueDate').value = defaultDue.toISOString().split('T')[0];
      } else {
        showToast('Gagal mencatat peminjaman', 'error');
      }
    }

    // ==================== RETURN ====================
    function renderReturn() {
      const content = document.getElementById('contentArea');
      const overdueBorrowings = allData.borrowings.filter(b => !b.returned && getDaysOverdue(b.dueDate) > 0);
      
      content.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Form Pengembalian</h3>
            <form id="returnForm" onsubmit="processReturn(event)">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Scan Barcode ISBN / Cari Peminjaman</label>
                  <div class="flex gap-2">
                    <input type="text" id="returnSearch" class="input-field" placeholder="Scan barcode atau ketik dan tekan Enter" onkeypress="handleReturnKeyPress(event)" oninput="searchBorrowings()">
                  </div>
                </div>
                <div id="borrowingSearchResults" class="space-y-2 max-h-64 overflow-y-auto"></div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Peminjaman Dipilih</label>
                  <div id="selectedBorrowing" class="p-3 bg-gray-50 rounded-lg text-gray-500">Belum ada peminjaman dipilih</div>
                  <input type="hidden" id="selectedBorrowingId">
                </div>
              </div>
              <button type="submit" class="btn-primary w-full mt-6">Proses Pengembalian</button>
            </form>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4 text-red-600">Buku Terlambat (${overdueBorrowings.length})</h3>
            <div class="space-y-3 max-h-96 overflow-y-auto">
              ${overdueBorrowings.length === 0 ? 
                '<p class="text-gray-500 text-center py-4">Tidak ada buku terlambat</p>' :
                overdueBorrowings.map(b => {
                  const overdue = getDaysOverdue(b.dueDate);
                  const finePerDay = allData.settings?.finePerDay || 1000;
                  const fine = overdue * finePerDay;
                  return `
                    <div class="p-4 bg-red-50 rounded-lg border border-red-200">
                      <div class="flex justify-between items-start">
                        <div>
                          <p class="font-medium text-gray-800">${b.bookTitle}</p>
                          <p class="text-sm text-gray-500">${b.memberName || 'Anggota'}</p>
                          <p class="text-xs text-gray-400 mt-1">Jatuh tempo: ${formatDate(b.dueDate)}</p>
                          <p class="text-sm text-red-600 font-medium mt-1">Denda: ${formatCurrency(fine)}</p>
                        </div>
                        <button onclick="selectBorrowing('${b.__backendId}')" class="btn-secondary text-sm">Pilih</button>
                      </div>
                    </div>
                  `;
                }).join('')
              }
            </div>
          </div>
        </div>
      `;
    }

    function handleReturnKeyPress(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        const search = document.getElementById('returnSearch').value.toLowerCase().trim();
        
        if (search.length < 2) {
          showToast('Masukkan minimal 2 karakter untuk mencari', 'error');
          return;
        }
        
        // Search for active borrowings
        const results = allData.borrowings.filter(b => 
          !b.returned && (
            (b.bookTitle || '').toLowerCase().includes(search) ||
            (b.bookIsbn || '').toLowerCase().includes(search) ||
            (b.memberId || '').toLowerCase().includes(search) ||
            (b.memberName || '').toLowerCase().includes(search)
          )
        );
        
        // Check for exact ISBN match first (for barcode scanning)
        const exactIsbnMatch = results.find(b => 
          (b.bookIsbn || '').toLowerCase() === search
        );
        
        if (exactIsbnMatch) {
          // Auto-select if exact ISBN match
          selectBorrowing(exactIsbnMatch.__backendId);
          document.getElementById('returnSearch').value = '';
          document.getElementById('borrowingSearchResults').innerHTML = '';
          showToast('Peminjaman dipilih: ' + exactIsbnMatch.bookTitle, 'info');
          return;
        }
        
        // Otherwise show search results
        searchBorrowings();
        
        // If only one result, auto-select it
        if (results.length === 1) {
          selectBorrowing(results[0].__backendId);
          document.getElementById('returnSearch').value = '';
          document.getElementById('borrowingSearchResults').innerHTML = '';
          showToast('Peminjaman dipilih: ' + results[0].bookTitle, 'info');
        } else if (results.length === 0) {
          showToast('Peminjaman tidak ditemukan', 'error');
        }
      }
    }

    function searchBorrowings() {
      const search = document.getElementById('returnSearch').value.toLowerCase();
      const resultsEl = document.getElementById('borrowingSearchResults');
      
      if (search.length < 2) {
        resultsEl.innerHTML = '';
        return;
      }
      
      const results = allData.borrowings.filter(b => 
        !b.returned && (
          (b.bookTitle || '').toLowerCase().includes(search) ||
          (b.bookIsbn || '').toLowerCase().includes(search) ||
          (b.memberId || '').toLowerCase().includes(search) ||
          (b.memberName || '').toLowerCase().includes(search)
        )
      ).slice(0, 5);
      
      resultsEl.innerHTML = results.length === 0 ? 
        '<p class="text-sm text-gray-500 p-2">Tidak ada peminjaman aktif ditemukan</p>' :
        results.map(b => {
          const overdue = getDaysOverdue(b.dueDate);
          return `
            <button type="button" onclick="selectBorrowing('${b.__backendId}')" class="w-full p-3 text-left hover:bg-blue-50 rounded border ${overdue > 0 ? 'border-red-200 bg-red-50' : 'border-gray-200'}">
              <span class="font-medium">${b.bookTitle}</span>
              <span class="text-sm text-gray-500 block">${b.memberName || 'Anggota'} • Jatuh tempo: ${formatDate(b.dueDate)}</span>
              ${overdue > 0 ? `<span class="text-sm text-red-600">${overdue} hari terlambat</span>` : ''}
            </button>
          `;
        }).join('');
    }

    function selectBorrowing(borrowingId) {
      const borrowing = allData.borrowings.find(b => b.__backendId === borrowingId);
      if (borrowing) {
        const overdue = getDaysOverdue(borrowing.dueDate);
        const finePerDay = allData.settings?.finePerDay || 1000;
        const fine = overdue * finePerDay;
        
        document.getElementById('selectedBorrowing').innerHTML = `
          <span class="font-medium">${borrowing.bookTitle}</span>
          <span class="text-sm text-gray-500 block">${borrowing.memberName || 'Anggota'}</span>
          <span class="text-sm text-gray-500 block">Dipinjam: ${formatDate(borrowing.borrowDate)} • Jatuh tempo: ${formatDate(borrowing.dueDate)}</span>
          ${overdue > 0 ? `<span class="text-sm text-red-600 block mt-1">Terlambat ${overdue} hari • Denda: ${formatCurrency(fine)}</span>` : '<span class="text-sm text-green-600 block mt-1">Tepat waktu</span>'}
        `;
        document.getElementById('selectedBorrowingId').value = borrowingId;
        document.getElementById('borrowingSearchResults').innerHTML = '';
        document.getElementById('returnSearch').value = '';
      }
    }

    async function processReturn(e) {
      e.preventDefault();
      
      const borrowingId = document.getElementById('selectedBorrowingId').value;
      if (!borrowingId) {
        showToast('Silakan pilih peminjaman terlebih dahulu', 'error');
        return;
      }
      
      const borrowing = allData.borrowings.find(b => b.__backendId === borrowingId);
      if (!borrowing) {
        showToast('Peminjaman tidak ditemukan', 'error');
        return;
      }
      
      const overdue = getDaysOverdue(borrowing.dueDate);
      const finePerDay = allData.settings?.finePerDay || 1000;
      const fine = overdue * finePerDay;
      
      // Update borrowing record
      const result = await window.dataSdk.update({
        ...borrowing,
        returned: true,
        returnDate: new Date().toISOString(),
        fine: fine
      });
      
      if (result.isOk) {
        // Update book availability
        const book = allData.books.find(b => b.__backendId === borrowing.bookId);
        if (book) {
          await window.dataSdk.update({ ...book, available: (book.available || 0) + 1 });
        }
        
        // Record fine as income if applicable
        if (fine > 0) {
          await window.dataSdk.create({
            type: 'income',
            source: 'Denda Keterlambatan',
            amount: fine,
            description: `Denda keterlambatan ${borrowing.bookTitle} - ${borrowing.memberName}`,
            transactionDate: new Date().toISOString()
          });
        }
        
        showToast(`Pengembalian berhasil${fine > 0 ? `. Denda: ${formatCurrency(fine)}` : ''}`);
        document.getElementById('selectedBorrowing').innerHTML = 'Belum ada peminjaman dipilih';
        document.getElementById('selectedBorrowingId').value = '';
      } else {
        showToast('Gagal memproses pengembalian', 'error');
      }
    }

    // ==================== VISIT ====================
    function renderVisit() {
      const content = document.getElementById('contentArea');
      const today = new Date().toISOString().split('T')[0];
      const todayVisits = allData.visits.filter(v => v.visitDate === today);
      
      content.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Catat Kunjungan</h3>
            <form id="visitForm" onsubmit="processVisit(event)">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">ID Anggota / NIS / NIP / Nama</label>
                  <div class="flex gap-2">
                    <input type="text" id="visitMemberId" class="input-field" placeholder="Scan barcode atau masukkan data" required>
                    <button type="button" onclick="searchVisitMember()" class="btn-secondary">${getIcon('search', 'w-5 h-5')}</button>
                  </div>
                  <p id="visitMemberInfo" class="text-sm text-gray-500 mt-1"></p>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Tujuan Kunjungan</label>
                  <select id="visitPurpose" class="input-field" required>
                    <option value="">Pilih Tujuan</option>
                    <option value="Membaca">Membaca</option>
                    <option value="Belajar">Belajar</option>
                    <option value="Mengerjakan Tugas">Mengerjakan Tugas</option>
                    <option value="Meminjam Buku">Meminjam Buku</option>
                    <option value="Mengembalikan Buku">Mengembalikan Buku</option>
                    <option value="Lainnya">Lainnya</option>
                  </select>
                </div>
                <div id="customPurposeContainer" class="hidden">
                  <label class="block text-sm font-medium text-gray-700 mb-1">Tujuan Lainnya</label>
                  <input type="text" id="customPurpose" class="input-field" placeholder="Masukkan tujuan">
                </div>
              </div>
              <button type="submit" class="btn-primary w-full mt-6">Catat Kunjungan</button>
            </form>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Kunjungan Hari Ini (${todayVisits.length})</h3>
            <div class="space-y-3 max-h-96 overflow-y-auto">
              ${todayVisits.length === 0 ? 
                '<p class="text-gray-500 text-center py-4">Belum ada kunjungan hari ini</p>' :
                todayVisits.map(v => `
                  <div class="p-3 bg-gray-50 rounded-lg flex items-center justify-between">
                    <div>
                      <p class="font-medium text-gray-800">${v.visitorName}</p>
                      <p class="text-sm text-gray-500">${v.purpose}</p>
                    </div>
                    <span class="text-sm text-gray-400">${v.visitTime}</span>
                  </div>
                `).join('')
              }
            </div>
          </div>
        </div>
      `;
      
      document.getElementById('visitPurpose').addEventListener('change', function() {
        const customContainer = document.getElementById('customPurposeContainer');
        customContainer.classList.toggle('hidden', this.value !== 'Lainnya');
      });
    }

    function searchVisitMember() {
      const id = document.getElementById('visitMemberId').value.trim();
      const member = allData.members.find(m => 
        m.nis === id || 
        m.__backendId === id || 
        m.name.toLowerCase().includes(id.toLowerCase())
      );
      const infoEl = document.getElementById('visitMemberInfo');
      const inputEl = document.getElementById('visitMemberId');
      
      if (member) {
        infoEl.innerHTML = `<span class="text-green-600">✓ ${member.name} (${member.role || 'Siswa'} - ${member.class || '-'})</span>`;
        inputEl.dataset.memberId = member.__backendId;
        inputEl.dataset.memberName = member.name;
      } else {
        infoEl.innerHTML = `<span class="text-yellow-600">⚠ Anggota tidak ditemukan, akan dicatat sebagai pengunjung umum</span>`;
        inputEl.dataset.memberId = '';
        inputEl.dataset.memberName = id;
      }
    }

    async function processVisit(e) {
      e.preventDefault();
      
      const inputEl = document.getElementById('visitMemberId');
      const visitorId = inputEl.dataset.memberId || '';
      const visitorName = inputEl.dataset.memberName || inputEl.value.trim();
      let purpose = document.getElementById('visitPurpose').value;
      
      if (purpose === 'Lainnya') {
        purpose = document.getElementById('customPurpose').value || 'Lainnya';
      }
      
      if (!visitorName) {
        showToast('Silakan masukkan data pengunjung', 'error');
        return;
      }
      
      const now = new Date();
      const visitData = {
        type: 'visit',
        visitorId: visitorId,
        visitorName: visitorName,
        visitDate: now.toISOString().split('T')[0],
        visitTime: now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' }),
        purpose: purpose
      };
      
      const result = await window.dataSdk.create(visitData);
      if (result.isOk) {
        showToast('Kunjungan berhasil dicatat');
        e.target.reset();
        document.getElementById('visitMemberInfo').innerHTML = '';
        delete inputEl.dataset.memberId;
        delete inputEl.dataset.memberName;
        document.getElementById('customPurposeContainer').classList.add('hidden');
      } else {
        showToast('Gagal mencatat kunjungan', 'error');
      }
    }

    // ==================== HISTORY ====================
    function renderHistory() {
      const content = document.getElementById('contentArea');
      const isAdmin = currentUser.isAdmin;
      
      let borrowings = allData.borrowings;
      let visits = allData.visits;
      
      // Filter for non-admin users
      if (!isAdmin) {
        const memberIds = [currentUser.__backendId, currentUser.nis];
        borrowings = borrowings.filter(b => memberIds.includes(b.memberId));
        visits = visits.filter(v => memberIds.includes(v.visitorId));
      }
      
      content.innerHTML = `
        <div class="mb-6">
          <div class="flex gap-2 border-b">
            <button onclick="showHistoryTab('borrowing')" id="tab-borrowing" class="px-4 py-2 border-b-2 border-blue-500 text-blue-600 font-medium">Peminjaman</button>
            <button onclick="showHistoryTab('return')" id="tab-return" class="px-4 py-2 border-b-2 border-transparent text-gray-500 hover:text-gray-700">Pengembalian</button>
            <button onclick="showHistoryTab('visit')" id="tab-visit" class="px-4 py-2 border-b-2 border-transparent text-gray-500 hover:text-gray-700">Kunjungan</button>
          </div>
        </div>
        
        <div class="card p-6">
          <div id="historyContent"></div>
        </div>
      `;
      
      window.historyData = { borrowings, visits };
      showHistoryTab('borrowing');
    }

    function showHistoryTab(tab) {
      const tabs = ['borrowing', 'return', 'visit'];
      tabs.forEach(t => {
        const tabEl = document.getElementById(`tab-${t}`);
        if (tabEl) {
          tabEl.className = t === tab ? 
            'px-4 py-2 border-b-2 border-blue-500 text-blue-600 font-medium' : 
            'px-4 py-2 border-b-2 border-transparent text-gray-500 hover:text-gray-700';
        }
      });
      
      const contentEl = document.getElementById('historyContent');
      const { borrowings, visits } = window.historyData;
      
      if (tab === 'borrowing') {
        const data = borrowings.filter(b => !b.returned);
        contentEl.innerHTML = renderHistoryTable(data, 'borrowing');
      } else if (tab === 'return') {
        const data = borrowings.filter(b => b.returned);
        contentEl.innerHTML = renderHistoryTable(data, 'return');
      } else {
        contentEl.innerHTML = renderHistoryTable(visits, 'visit');
      }
    }

    function renderHistoryTable(data, type) {
      if (data.length === 0) {
        return '<p class="text-gray-500 text-center py-8">Tidak ada data</p>';
      }
      
      if (type === 'borrowing' || type === 'return') {
        return `
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Tanggal Pinjam</th>
                  <th>Buku</th>
                  <th>Anggota</th>
                  <th>Jatuh Tempo</th>
                  ${type === 'return' ? '<th>Tanggal Kembali</th><th>Denda</th>' : '<th>Status</th>'}
                </tr>
              </thead>
              <tbody>
                ${data.map(b => {
                  const overdue = !b.returned ? getDaysOverdue(b.dueDate) : 0;
                  return `
                    <tr>
                      <td>${formatDate(b.borrowDate)}</td>
                      <td class="font-medium">${b.bookTitle}</td>
                      <td>${b.memberName || '-'}</td>
                      <td>${formatDate(b.dueDate)}</td>
                      ${type === 'return' ? 
                        `<td>${formatDate(b.returnDate)}</td><td>${b.fine ? formatCurrency(b.fine) : '-'}</td>` :
                        `<td><span class="badge ${overdue > 0 ? 'badge-danger' : 'badge-success'}">${overdue > 0 ? overdue + ' hari terlambat' : 'Aktif'}</span></td>`
                      }
                    </tr>
                  `;
                }).join('')}
              </tbody>
            </table>
          </div>
        `;
      } else {
        return `
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Tanggal</th>
                  <th>Waktu</th>
                  <th>Pengunjung</th>
                  <th>Tujuan</th>
                </tr>
              </thead>
              <tbody>
                ${data.map(v => `
                  <tr>
                    <td>${formatDate(v.visitDate)}</td>
                    <td>${v.visitTime}</td>
                    <td class="font-medium">${v.visitorName}</td>
                    <td>${v.purpose}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        `;
      }
    }

    // ==================== REPORTS ====================
    function renderReports() {
      const content = document.getElementById('contentArea');
      
      // Calculate statistics
      const bookBorrowCount = {};
      const memberBorrowCount = {};
      const memberVisitCount = {};
      const categoryCount = {};
      
      allData.borrowings.forEach(b => {
        bookBorrowCount[b.bookTitle] = (bookBorrowCount[b.bookTitle] || 0) + 1;
        memberBorrowCount[b.memberName] = (memberBorrowCount[b.memberName] || 0) + 1;
      });
      
      allData.visits.forEach(v => {
        memberVisitCount[v.visitorName] = (memberVisitCount[v.visitorName] || 0) + 1;
      });
      
      allData.books.forEach(b => {
        const cat = b.category || 'Lainnya';
        categoryCount[cat] = (categoryCount[cat] || 0) + (b.stock || 0);
      });
      
      const topBooks = Object.entries(bookBorrowCount).sort((a, b) => b[1] - a[1]).slice(0, 10);
      const topBorrowers = Object.entries(memberBorrowCount).sort((a, b) => b[1] - a[1]).slice(0, 10);
      const topVisitors = Object.entries(memberVisitCount).sort((a, b) => b[1] - a[1]).slice(0, 10);
      
      const totalIncome = allData.income.reduce((sum, i) => sum + (i.amount || 0), 0);
      const totalExpense = allData.expenses.reduce((sum, e) => sum + (e.amount || 0), 0);
      
      // Chart data for categories
      const categoryEntries = Object.entries(categoryCount).sort((a, b) => b[1] - a[1]);
      const maxCategoryValue = Math.max(...categoryEntries.map(c => c[1]), 1);
      
      content.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
          <div class="card p-6">
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-bold text-gray-800">Periode Laporan</h3>
            </div>
            <div class="grid grid-cols-2 gap-4 mb-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Dari Tanggal</label>
                <input type="date" id="reportStartDate" class="input-field">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Sampai Tanggal</label>
                <input type="date" id="reportEndDate" class="input-field">
              </div>
            </div>
            <div class="space-y-3">
              <div>
                <p class="text-sm font-medium text-gray-700 mb-2">Download ke Perangkat:</p>
                <div class="flex gap-2">
                  <button onclick="exportReport('csv', 'download')" class="btn-secondary flex items-center gap-2 flex-1">${getIcon('download', 'w-4 h-4')} CSV</button>
                  <button onclick="exportReport('pdf', 'download')" class="btn-primary flex items-center gap-2 flex-1">${getIcon('download', 'w-4 h-4')} PDF</button>
                </div>
              </div>
            </div>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Ringkasan Keuangan</h3>
            <div class="space-y-3">
              <div class="flex justify-between items-center p-3 bg-green-50 rounded-lg">
                <span class="text-green-700">Total Pemasukan</span>
                <span class="font-bold text-green-700">${formatCurrency(totalIncome)}</span>
              </div>
              <div class="flex justify-between items-center p-3 bg-red-50 rounded-lg">
                <span class="text-red-700">Total Pengeluaran</span>
                <span class="font-bold text-red-700">${formatCurrency(totalExpense)}</span>
              </div>
              <div class="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                <span class="text-blue-700">Saldo</span>
                <span class="font-bold text-blue-700">${formatCurrency(totalIncome - totalExpense)}</span>
              </div>
            </div>
            <div class="mt-4">
              <p class="text-sm font-medium text-gray-700 mb-2">Download Laporan Keuangan:</p>
              <div class="flex gap-2">
                <button onclick="exportFinance('csv', 'download')" class="btn-secondary flex items-center gap-2 text-sm flex-1">${getIcon('download', 'w-4 h-4')} CSV</button>
                <button onclick="exportFinance('pdf', 'download')" class="btn-primary flex items-center gap-2 text-sm flex-1">${getIcon('download', 'w-4 h-4')} PDF</button>
              </div>
            </div>
          </div>
        </div>
        
        <div class="card p-6 mb-6">
          <h3 class="text-lg font-bold text-gray-800 mb-4">📊 Distribusi Buku per Kategori</h3>
          <div class="space-y-3">
            ${categoryEntries.length === 0 ? 
              '<p class="text-gray-500 text-center py-4">Belum ada data buku</p>' :
              categoryEntries.map(([category, count]) => {
                const percentage = (count / maxCategoryValue) * 100;
                const colors = ['bg-blue-500', 'bg-green-500', 'bg-yellow-500', 'bg-purple-500', 'bg-pink-500', 'bg-indigo-500', 'bg-red-500', 'bg-teal-500', 'bg-orange-500'];
                const colorIndex = categoryEntries.findIndex(c => c[0] === category) % colors.length;
                const barColor = colors[colorIndex];
                
                return `
                  <div>
                    <div class="flex justify-between mb-1">
                      <span class="text-sm font-medium text-gray-700">${category}</span>
                      <span class="text-sm font-bold text-gray-900">${count} buku</span>
                    </div>
                    <div class="w-full bg-gray-200 rounded-full h-4 overflow-hidden">
                      <div class="${barColor} h-4 rounded-full transition-all duration-500" style="width: ${percentage}%"></div>
                    </div>
                  </div>
                `;
              }).join('')
            }
          </div>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">📚 Buku Paling Banyak Dipinjam</h3>
            <div class="space-y-2">
              ${topBooks.length === 0 ? '<p class="text-gray-500 text-center py-4">Belum ada data</p>' :
                topBooks.map((b, i) => `
                  <div class="flex items-center gap-3 p-2 rounded hover:bg-gray-50">
                    <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-xs font-bold">${i + 1}</span>
                    <span class="flex-1 text-sm truncate">${b[0]}</span>
                    <span class="text-sm font-medium text-gray-500">${b[1]}x</span>
                  </div>
                `).join('')
              }
            </div>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">📖 Peminjam Paling Aktif</h3>
            <div class="space-y-2">
              ${topBorrowers.length === 0 ? '<p class="text-gray-500 text-center py-4">Belum ada data</p>' :
                topBorrowers.map((m, i) => `
                  <div class="flex items-center gap-3 p-2 rounded hover:bg-gray-50">
                    <span class="w-6 h-6 rounded-full bg-green-100 text-green-600 flex items-center justify-center text-xs font-bold">${i + 1}</span>
                    <span class="flex-1 text-sm truncate">${m[0]}</span>
                    <span class="text-sm font-medium text-gray-500">${m[1]}x</span>
                  </div>
                `).join('')
              }
            </div>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">🚶 Pengunjung Paling Aktif</h3>
            <div class="space-y-2">
              ${topVisitors.length === 0 ? '<p class="text-gray-500 text-center py-4">Belum ada data</p>' :
                topVisitors.map((v, i) => `
                  <div class="flex items-center gap-3 p-2 rounded hover:bg-gray-50">
                    <span class="w-6 h-6 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center text-xs font-bold">${i + 1}</span>
                    <span class="flex-1 text-sm truncate">${v[0]}</span>
                    <span class="text-sm font-medium text-gray-500">${v[1]}x</span>
                  </div>
                `).join('')
              }
            </div>
          </div>
        </div>
      `;
    }

    function exportReport(format) {
      const startDate = document.getElementById('reportStartDate').value;
      const endDate = document.getElementById('reportEndDate').value;
      
      let filteredBorrowings = allData.borrowings;
      let filteredVisits = allData.visits;
      
      if (startDate) {
        filteredBorrowings = filteredBorrowings.filter(b => {
          const borrowDate = b.borrowDate.split('T')[0];
          return borrowDate >= startDate;
        });
        filteredVisits = filteredVisits.filter(v => v.visitDate >= startDate);
      }
      if (endDate) {
        filteredBorrowings = filteredBorrowings.filter(b => {
          const borrowDate = b.borrowDate.split('T')[0];
          return borrowDate <= endDate;
        });
        filteredVisits = filteredVisits.filter(v => v.visitDate <= endDate);
      }
      
      if (format === 'csv') {
        const settings = allData.settings || {};
        let csv = `"LAPORAN PERPUSTAKAAN"\n`;
        csv += `"${settings.schoolName || 'Perpustakaan'}"\n`;
        csv += `"Periode: ${startDate ? formatDate(startDate) : 'Awal'} s/d ${endDate ? formatDate(endDate) : 'Akhir'}"\n\n`;
        
        csv += '"PEMINJAMAN BUKU"\n';
        csv += '"No","Tanggal Pinjam","ISBN","Judul Buku","NIS/NIP","Nama Anggota","Jatuh Tempo","Tanggal Kembali","Status","Denda"\n';
        filteredBorrowings.forEach((b, i) => {
          csv += `"${i+1}","${formatDate(b.borrowDate)}","${b.bookIsbn || '-'}","${b.bookTitle}","${b.memberId}","${b.memberName}","${formatDate(b.dueDate)}","${b.returned ? formatDate(b.returnDate) : '-'}","${b.returned ? 'Dikembalikan' : 'Dipinjam'}","${formatCurrency(b.fine || 0)}"\n`;
        });
        
        csv += '\n"KUNJUNGAN PERPUSTAKAAN"\n';
        csv += '"No","Tanggal","Waktu","ID Pengunjung","Nama Pengunjung","Tujuan"\n';
        filteredVisits.forEach((v, i) => {
          csv += `"${i+1}","${formatDate(v.visitDate)}","${v.visitTime}","${v.visitorId || '-'}","${v.visitorName}","${v.purpose}"\n`;
        });
        
        csv += '\n"RINGKASAN"\n';
        csv += `"Total Peminjaman","${filteredBorrowings.length}"\n`;
        csv += `"Total Kunjungan","${filteredVisits.length}"\n`;
        csv += `"Total Denda","${formatCurrency(filteredBorrowings.reduce((sum, b) => sum + (b.fine || 0), 0))}"\n`;
        
        downloadFile(csv, `laporan_perpustakaan_${new Date().toISOString().split('T')[0]}.csv`, 'text/csv;charset=utf-8;');
        showToast('Laporan CSV berhasil didownload ke perangkat');
      } else {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        const settings = allData.settings || {};
        
        // Header
        doc.setFontSize(18);
        doc.setFont(undefined, 'bold');
        doc.text('LAPORAN PERPUSTAKAAN', 105, 20, { align: 'center' });
        doc.setFontSize(12);
        doc.setFont(undefined, 'normal');
        doc.text(settings.schoolName || 'Perpustakaan', 105, 28, { align: 'center' });
        doc.setFontSize(10);
        doc.text(`Periode: ${startDate ? formatDate(startDate) : 'Awal'} s/d ${endDate ? formatDate(endDate) : 'Akhir'}`, 105, 35, { align: 'center' });
        
        // Line separator
        doc.setLineWidth(0.5);
        doc.line(20, 40, 190, 40);
        
        let y = 50;
        
        // Peminjaman Section
        doc.setFontSize(14);
        doc.setFont(undefined, 'bold');
        doc.text('PEMINJAMAN BUKU', 20, y);
        y += 8;
        
        doc.setFontSize(9);
        doc.setFont(undefined, 'normal');
        
        if (filteredBorrowings.length === 0) {
          doc.text('Tidak ada data peminjaman', 20, y);
          y += 10;
        } else {
          const borrowingsToShow = filteredBorrowings.slice(0, 20);
          borrowingsToShow.forEach((b, i) => {
            if (y > 270) {
              doc.addPage();
              y = 20;
            }
            const status = b.returned ? 'Kembali' : 'Pinjam';
            const denda = b.fine ? formatCurrency(b.fine) : '-';
            doc.text(`${i+1}. ${formatDate(b.borrowDate)} | ${b.bookTitle}`, 20, y);
            y += 5;
            doc.text(`   ${b.memberName} | ${status} | Denda: ${denda}`, 20, y);
            y += 7;
          });
          
          if (filteredBorrowings.length > 20) {
            doc.setFont(undefined, 'italic');
            doc.text(`... dan ${filteredBorrowings.length - 20} data lainnya`, 20, y);
            doc.setFont(undefined, 'normal');
            y += 10;
          }
        }
        
        // Kunjungan Section
        if (y > 200) {
          doc.addPage();
          y = 20;
        }
        
        doc.setFontSize(14);
        doc.setFont(undefined, 'bold');
        doc.text('KUNJUNGAN PERPUSTAKAAN', 20, y);
        y += 8;
        
        doc.setFontSize(9);
        doc.setFont(undefined, 'normal');
        
        if (filteredVisits.length === 0) {
          doc.text('Tidak ada data kunjungan', 20, y);
          y += 10;
        } else {
          const visitsToShow = filteredVisits.slice(0, 20);
          visitsToShow.forEach((v, i) => {
            if (y > 270) {
              doc.addPage();
              y = 20;
            }
            doc.text(`${i+1}. ${formatDate(v.visitDate)} ${v.visitTime} | ${v.visitorName} | ${v.purpose}`, 20, y);
            y += 6;
          });
          
          if (filteredVisits.length > 20) {
            doc.setFont(undefined, 'italic');
            doc.text(`... dan ${filteredVisits.length - 20} data lainnya`, 20, y);
            doc.setFont(undefined, 'normal');
            y += 10;
          }
        }
        
        // Summary
        if (y > 240) {
          doc.addPage();
          y = 20;
        }
        
        y += 5;
        doc.setLineWidth(0.5);
        doc.line(20, y, 190, y);
        y += 8;
        
        doc.setFontSize(12);
        doc.setFont(undefined, 'bold');
        doc.text('RINGKASAN', 20, y);
        y += 8;
        
        doc.setFontSize(10);
        doc.setFont(undefined, 'normal');
        doc.text(`Total Peminjaman: ${filteredBorrowings.length}`, 20, y);
        y += 6;
        doc.text(`Total Kunjungan: ${filteredVisits.length}`, 20, y);
        y += 6;
        const totalDenda = filteredBorrowings.reduce((sum, b) => sum + (b.fine || 0), 0);
        doc.text(`Total Denda: ${formatCurrency(totalDenda)}`, 20, y);
        
        // Footer
        const pageCount = doc.internal.getNumberOfPages();
        for (let i = 1; i <= pageCount; i++) {
          doc.setPage(i);
          doc.setFontSize(8);
          doc.text(`Halaman ${i} dari ${pageCount}`, 105, 290, { align: 'center' });
          doc.text(`Dicetak: ${formatDate(new Date().toISOString())} ${new Date().toLocaleTimeString('id-ID')}`, 190, 290, { align: 'right' });
        }
        
        doc.save(`laporan_perpustakaan_${new Date().toISOString().split('T')[0]}.pdf`);
        showToast('Laporan PDF berhasil didownload ke perangkat');
      }
    }

    function exportFinance(format) {
      const allTransactions = [
        ...allData.income.map(i => ({ ...i, type: 'Pemasukan' })),
        ...allData.expenses.map(e => ({ ...e, type: 'Pengeluaran' }))
      ].sort((a, b) => new Date(b.transactionDate) - new Date(a.transactionDate));
      
      const totalIncome = allData.income.reduce((sum, i) => sum + (i.amount || 0), 0);
      const totalExpense = allData.expenses.reduce((sum, e) => sum + (e.amount || 0), 0);
      const balance = totalIncome - totalExpense;
      
      if (format === 'csv') {
        const settings = allData.settings || {};
        let csv = `"LAPORAN KEUANGAN PERPUSTAKAAN"\n`;
        csv += `"${settings.schoolName || 'Perpustakaan'}"\n`;
        csv += `"Dicetak: ${formatDate(new Date().toISOString())} ${new Date().toLocaleTimeString('id-ID')}"\n\n`;
        
        csv += '"RINGKASAN KEUANGAN"\n';
        csv += `"Total Pemasukan","${formatCurrency(totalIncome)}"\n`;
        csv += `"Total Pengeluaran","${formatCurrency(totalExpense)}"\n`;
        csv += `"Saldo","${formatCurrency(balance)}"\n\n`;
        
        csv += '"RINCIAN TRANSAKSI"\n';
        csv += '"No","Tanggal","Jenis","Sumber/Keterangan","Jumlah"\n';
        allTransactions.forEach((t, i) => {
          csv += `"${i+1}","${formatDate(t.transactionDate)}","${t.type}","${t.source || t.description}","${formatCurrency(t.amount)}"\n`;
        });
        
        csv += '\n"PEMASUKAN PER SUMBER"\n';
        const incomeBySource = {};
        allData.income.forEach(i => {
          incomeBySource[i.source] = (incomeBySource[i.source] || 0) + i.amount;
        });
        csv += '"Sumber","Jumlah"\n';
        Object.entries(incomeBySource).forEach(([source, amount]) => {
          csv += `"${source}","${formatCurrency(amount)}"\n`;
        });
        
        downloadFile(csv, `laporan_keuangan_${new Date().toISOString().split('T')[0]}.csv`, 'text/csv;charset=utf-8;');
        showToast('Laporan Keuangan CSV berhasil didownload ke perangkat');
      } else {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        const settings = allData.settings || {};
        
        // Header
        doc.setFontSize(18);
        doc.setFont(undefined, 'bold');
        doc.text('LAPORAN KEUANGAN', 105, 20, { align: 'center' });
        doc.setFontSize(12);
        doc.setFont(undefined, 'normal');
        doc.text(settings.schoolName || 'Perpustakaan', 105, 28, { align: 'center' });
        doc.setFontSize(9);
        doc.text(`Dicetak: ${formatDate(new Date().toISOString())} ${new Date().toLocaleTimeString('id-ID')}`, 105, 35, { align: 'center' });
        
        // Line separator
        doc.setLineWidth(0.5);
        doc.line(20, 40, 190, 40);
        
        let y = 50;
        
        // Summary Section
        doc.setFontSize(14);
        doc.setFont(undefined, 'bold');
        doc.text('RINGKASAN KEUANGAN', 20, y);
        y += 10;
        
        doc.setFontSize(11);
        doc.setFont(undefined, 'normal');
        
        // Summary boxes
        doc.setFillColor(220, 252, 231); // Green background
        doc.rect(20, y, 170, 10, 'F');
        doc.setTextColor(22, 101, 52); // Green text
        doc.text(`Total Pemasukan: ${formatCurrency(totalIncome)}`, 25, y + 7);
        y += 12;
        
        doc.setFillColor(254, 226, 226); // Red background
        doc.rect(20, y, 170, 10, 'F');
        doc.setTextColor(153, 27, 27); // Red text
        doc.text(`Total Pengeluaran: ${formatCurrency(totalExpense)}`, 25, y + 7);
        y += 12;
        
        doc.setFillColor(219, 234, 254); // Blue background
        doc.rect(20, y, 170, 10, 'F');
        doc.setTextColor(30, 64, 175); // Blue text
        doc.setFont(undefined, 'bold');
        doc.text(`Saldo: ${formatCurrency(balance)}`, 25, y + 7);
        doc.setFont(undefined, 'normal');
        y += 20;
        
        doc.setTextColor(0, 0, 0); // Reset to black
        
        // Transaction Details
        doc.setFontSize(14);
        doc.setFont(undefined, 'bold');
        doc.text('RINCIAN TRANSAKSI', 20, y);
        y += 8;
        
        doc.setFontSize(9);
        doc.setFont(undefined, 'normal');
        
        if (allTransactions.length === 0) {
          doc.text('Tidak ada transaksi', 20, y);
        } else {
          const transactionsToShow = allTransactions.slice(0, 25);
          transactionsToShow.forEach((t, i) => {
            if (y > 270) {
              doc.addPage();
              y = 20;
            }
            
            const typeColor = t.type === 'Pemasukan' ? [34, 197, 94] : [239, 68, 68];
            doc.setTextColor(...typeColor);
            doc.setFont(undefined, 'bold');
            doc.text(`${i+1}. ${t.type}`, 20, y);
            doc.setTextColor(0, 0, 0);
            doc.setFont(undefined, 'normal');
            
            y += 5;
            doc.text(`   ${formatDate(t.transactionDate)} | ${t.source || t.description}`, 20, y);
            y += 5;
            doc.setFont(undefined, 'bold');
            doc.text(`   ${formatCurrency(t.amount)}`, 20, y);
            doc.setFont(undefined, 'normal');
            y += 7;
          });
          
          if (allTransactions.length > 25) {
            doc.setFont(undefined, 'italic');
            doc.text(`... dan ${allTransactions.length - 25} transaksi lainnya`, 20, y);
            doc.setFont(undefined, 'normal');
            y += 8;
          }
        }
        
        // Income by Source
        if (y > 200) {
          doc.addPage();
          y = 20;
        }
        
        y += 5;
        doc.setLineWidth(0.5);
        doc.line(20, y, 190, y);
        y += 8;
        
        doc.setFontSize(12);
        doc.setFont(undefined, 'bold');
        doc.text('PEMASUKAN PER SUMBER', 20, y);
        y += 8;
        
        doc.setFontSize(9);
        doc.setFont(undefined, 'normal');
        
        const incomeBySource = {};
        allData.income.forEach(i => {
          incomeBySource[i.source] = (incomeBySource[i.source] || 0) + i.amount;
        });
        
        Object.entries(incomeBySource).forEach(([source, amount]) => {
          if (y > 270) {
            doc.addPage();
            y = 20;
          }
          doc.text(`• ${source}: ${formatCurrency(amount)}`, 25, y);
          y += 6;
        });
        
        // Footer
        const pageCount = doc.internal.getNumberOfPages();
        for (let i = 1; i <= pageCount; i++) {
          doc.setPage(i);
          doc.setFontSize(8);
          doc.setTextColor(100, 100, 100);
          doc.text(`Halaman ${i} dari ${pageCount}`, 105, 290, { align: 'center' });
          doc.text(`${settings.schoolName || 'Perpustakaan'}`, 20, 290);
        }
        
        doc.save(`laporan_keuangan_${new Date().toISOString().split('T')[0]}.pdf`);
        showToast('Laporan Keuangan PDF berhasil didownload ke perangkat');
      }
    }

    function downloadFile(content, filename, type) {
      const blob = new Blob([content], { type });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      a.click();
      URL.revokeObjectURL(url);
    }

    // ==================== FINANCE ====================
    function renderFinance() {
      const content = document.getElementById('contentArea');
      const totalIncome = allData.income.reduce((sum, i) => sum + (i.amount || 0), 0);
      const totalExpense = allData.expenses.reduce((sum, e) => sum + (e.amount || 0), 0);
      
      content.innerHTML = `
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div class="stat-card" style="--stat-color: #10b981; --stat-color-dark: #059669;">
            <p class="text-green-100 text-sm">Total Pemasukan</p>
            <p class="text-2xl font-bold mt-1">${formatCurrency(totalIncome)}</p>
          </div>
          <div class="stat-card" style="--stat-color: #ef4444; --stat-color-dark: #dc2626;">
            <p class="text-red-100 text-sm">Total Pengeluaran</p>
            <p class="text-2xl font-bold mt-1">${formatCurrency(totalExpense)}</p>
          </div>
          <div class="stat-card" style="--stat-color: #3b82f6; --stat-color-dark: #1d4ed8;">
            <p class="text-blue-100 text-sm">Saldo</p>
            <p class="text-2xl font-bold mt-1">${formatCurrency(totalIncome - totalExpense)}</p>
          </div>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="card p-6">
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-bold text-gray-800 text-green-600">💰 Pemasukan</h3>
              <button onclick="showIncomeModal()" class="btn-primary text-sm">${getIcon('plus', 'w-4 h-4')} Tambah</button>
            </div>
            <div class="space-y-3 max-h-96 overflow-y-auto">
              ${allData.income.length === 0 ? 
                '<p class="text-gray-500 text-center py-4">Belum ada pemasukan</p>' :
                allData.income.map(i => `
                  <div class="p-3 bg-green-50 rounded-lg flex justify-between items-center">
                    <div>
                      <p class="font-medium text-gray-800">${i.source}</p>
                      <p class="text-sm text-gray-500">${i.description || '-'}</p>
                      <p class="text-xs text-gray-400">${formatDate(i.transactionDate)}</p>
                    </div>
                    <div class="text-right">
                      <p class="font-bold text-green-600">${formatCurrency(i.amount)}</p>
                      <button onclick="confirmDelete('income', '${i.__backendId}')" class="text-red-500 text-xs hover:underline">Hapus</button>
                    </div>
                  </div>
                `).join('')
              }
            </div>
          </div>
          
          <div class="card p-6">
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-bold text-gray-800 text-red-600">💸 Pengeluaran</h3>
              <button onclick="showExpenseModal()" class="btn-danger text-sm">${getIcon('plus', 'w-4 h-4')} Tambah</button>
            </div>
            <div class="space-y-3 max-h-96 overflow-y-auto">
              ${allData.expenses.length === 0 ? 
                '<p class="text-gray-500 text-center py-4">Belum ada pengeluaran</p>' :
                allData.expenses.map(e => `
                  <div class="p-3 bg-red-50 rounded-lg flex justify-between items-center">
                    <div>
                      <p class="font-medium text-gray-800">${e.description}</p>
                      <p class="text-xs text-gray-400">${formatDate(e.transactionDate)}</p>
                    </div>
                    <div class="text-right">
                      <p class="font-bold text-red-600">${formatCurrency(e.amount)}</p>
                      <button onclick="confirmDelete('expense', '${e.__backendId}')" class="text-red-500 text-xs hover:underline">Hapus</button>
                    </div>
                  </div>
                `).join('')
              }
            </div>
          </div>
        </div>
      `;
    }

    function showIncomeModal() {
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'incomeModal';
      modal.innerHTML = `
        <div class="modal-content p-6">
          <h2 class="text-xl font-bold mb-6">Tambah Pemasukan</h2>
          <form id="incomeForm" onsubmit="saveIncome(event)">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Sumber Pemasukan</label>
                <select name="source" class="input-field" required onchange="toggleCustomSource(this)">
                  <option value="">Pilih Sumber</option>
                  <option value="Denda Keterlambatan">Denda Keterlambatan</option>
                  <option value="Denda Pelanggaran Tata Tertib">Denda Pelanggaran Tata Tertib</option>
                  <option value="Lainnya">Lainnya (Custom)</option>
                </select>
              </div>
              <div id="customSourceContainer" class="hidden">
                <label class="block text-sm font-medium text-gray-700 mb-1">Sumber Custom</label>
                <input type="text" name="customSource" class="input-field" placeholder="Masukkan sumber pemasukan">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Jumlah (Rp)</label>
                <input type="number" name="amount" class="input-field" min="0" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Keterangan</label>
                <textarea name="description" class="input-field" rows="2"></textarea>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button type="submit" class="btn-primary flex-1">Simpan</button>
              <button type="button" onclick="closeModal('incomeModal')" class="btn-secondary">Batal</button>
            </div>
          </form>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    function toggleCustomSource(select) {
      const container = document.getElementById('customSourceContainer');
      container.classList.toggle('hidden', select.value !== 'Lainnya');
    }

    async function saveIncome(e) {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      
      let source = formData.get('source');
      if (source === 'Lainnya') {
        source = formData.get('customSource') || 'Lainnya';
      }
      
      const incomeData = {
        type: 'income',
        source: source,
        amount: parseInt(formData.get('amount')) || 0,
        description: formData.get('description'),
        transactionDate: new Date().toISOString()
      };
      
      const result = await window.dataSdk.create(incomeData);
      if (result.isOk) {
        showToast('Pemasukan berhasil ditambahkan');
        closeModal('incomeModal');
      } else {
        showToast('Gagal menambahkan pemasukan', 'error');
      }
    }

    function showExpenseModal() {
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'expenseModal';
      modal.innerHTML = `
        <div class="modal-content p-6">
          <h2 class="text-xl font-bold mb-6">Tambah Pengeluaran</h2>
          <form id="expenseForm" onsubmit="saveExpense(event)">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Jumlah (Rp)</label>
                <input type="number" name="amount" class="input-field" min="0" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Keterangan Pengeluaran</label>
                <textarea name="description" class="input-field" rows="3" required></textarea>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button type="submit" class="btn-primary flex-1">Simpan</button>
              <button type="button" onclick="closeModal('expenseModal')" class="btn-secondary">Batal</button>
            </div>
          </form>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    async function saveExpense(e) {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      
      const expenseData = {
        type: 'expense',
        amount: parseInt(formData.get('amount')) || 0,
        description: formData.get('description'),
        transactionDate: new Date().toISOString()
      };
      
      const result = await window.dataSdk.create(expenseData);
      if (result.isOk) {
        showToast('Pengeluaran berhasil ditambahkan');
        closeModal('expenseModal');
      } else {
        showToast('Gagal menambahkan pengeluaran', 'error');
      }
    }

    // ==================== SETTINGS ====================
    function renderSettings() {
      const content = document.getElementById('contentArea');
      const settings = allData.settings || {};
      
      content.innerHTML = `
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Informasi Perpustakaan</h3>
            <form id="settingsForm" onsubmit="saveSettings(event)">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Nama Sekolah/Institusi</label>
                  <input type="text" name="schoolName" class="input-field" value="${settings.schoolName || ''}" placeholder="Nama Sekolah">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Kepala Sekolah</label>
                  <input type="text" name="principal" class="input-field" value="${settings.principal || ''}" placeholder="Nama Kepala Sekolah">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Alamat</label>
                  <textarea name="schoolAddress" class="input-field" rows="2" placeholder="Alamat lengkap">${settings.schoolAddress || ''}</textarea>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Denda per Hari (Rp)</label>
                  <input type="number" name="finePerDay" class="input-field" value="${settings.finePerDay || 1000}" min="0">
                </div>
              </div>
              <button type="submit" class="btn-primary w-full mt-6">Simpan Pengaturan</button>
            </form>
          </div>
          
          <div class="card p-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Tampilan</h3>
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Logo Perpustakaan (URL Google Drive)</label>
                ${settings.logo ? `<div class="mb-3"><img src="${settings.logo}" class="w-24 h-24 object-cover rounded-lg border-2 border-gray-200"></div>` : ''}
                <input type="text" id="logoUrl" placeholder="Masukkan URL Google Drive logo" class="input-field" onchange="uploadLogoFromUrl(event)">
                <p class="text-xs text-gray-500 mt-1">Masukkan URL Google Drive untuk logo perpustakaan</p>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Background Aplikasi (URL Google Drive)</label>
                ${settings.background ? `<div class="mb-3"><img src="${settings.background}" class="w-full h-32 object-cover rounded-lg border-2 border-gray-200"></div>` : ''}
                <input type="text" id="bgUrl" placeholder="Masukkan URL Google Drive background" class="input-field" onchange="uploadBackgroundFromUrl(event)">
                <p class="text-xs text-gray-500 mt-1">Masukkan URL Google Drive untuk background aplikasi</p>
              </div>
            </div>
          </div>
        </div>
      `;
    }

    async function saveSettings(e) {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      
      const settingsData = {
        type: 'settings',
        schoolName: formData.get('schoolName'),
        principal: formData.get('principal'),
        schoolAddress: formData.get('schoolAddress'),
        finePerDay: parseInt(formData.get('finePerDay')) || 1000,
        logo: allData.settings?.logo || '',
        background: allData.settings?.background || ''
      };
      
      if (allData.settings) {
        const result = await window.dataSdk.update({ ...allData.settings, ...settingsData });
        if (result.isOk) {
          showToast('Pengaturan berhasil disimpan');
        }
      } else {
        const result = await window.dataSdk.create(settingsData);
        if (result.isOk) {
          showToast('Pengaturan berhasil disimpan');
        }
      }
    }

    async function uploadLogoFromUrl(e) {
      const url = e.target.value.trim();
      if (!url) return;
      
      const directUrl = convertGoogleDriveUrl(url);
      if (!directUrl) {
        showToast('URL tidak valid', 'error');
        return;
      }
      
      showToast('Mengupload logo dari URL...', 'info');
      
      if (allData.settings && allData.settings.__backendId) {
        const result = await window.dataSdk.update({ ...allData.settings, logo: directUrl });
        if (result.isOk) {
          showToast('Logo berhasil diupload');
          e.target.value = '';
          renderSettings();
        } else {
          showToast('Gagal mengupload logo', 'error');
        }
      } else {
        const settingsData = {
          type: 'settings',
          schoolName: '',
          principal: '',
          schoolAddress: '',
          finePerDay: 1000,
          logo: directUrl,
          background: ''
        };
        const result = await window.dataSdk.create(settingsData);
        if (result.isOk) {
          showToast('Logo berhasil diupload');
          e.target.value = '';
          renderSettings();
        } else {
          showToast('Gagal mengupload logo', 'error');
        }
      }
    }

    async function uploadBackgroundFromUrl(e) {
      const url = e.target.value.trim();
      if (!url) return;
      
      const directUrl = convertGoogleDriveUrl(url);
      if (!directUrl) {
        showToast('URL tidak valid', 'error');
        return;
      }
      
      showToast('Mengupload background dari URL...', 'info');
      
      if (allData.settings && allData.settings.__backendId) {
        const result = await window.dataSdk.update({ ...allData.settings, background: directUrl });
        if (result.isOk) {
          showToast('Background berhasil diupload');
          e.target.value = '';
          renderSettings();
        } else {
          showToast('Gagal mengupload background', 'error');
        }
      } else {
        const settingsData = {
          type: 'settings',
          schoolName: '',
          principal: '',
          schoolAddress: '',
          finePerDay: 1000,
          logo: '',
          background: directUrl
        };
        const result = await window.dataSdk.create(settingsData);
        if (result.isOk) {
          showToast('Background berhasil diupload');
          e.target.value = '';
          renderSettings();
        } else {
          showToast('Gagal mengupload background', 'error');
        }
      }
    }

    // ==================== EBOOKS ====================
    function renderEbooks() {
      const content = document.getElementById('contentArea');
      const isAdmin = currentUser.isAdmin;
      
      content.innerHTML = `
        <div class="card p-6 mb-6">
          <div class="flex flex-wrap gap-4 items-center justify-between mb-6">
            <h3 class="text-lg font-bold text-gray-800">Koleksi Buku Digital</h3>
            ${isAdmin ? `
              <button onclick="showPdfUploadModal()" class="btn-primary flex items-center gap-2">
                ${getIcon('plus', 'w-5 h-5')} Import PDF dari Perangkat
              </button>
            ` : ''}
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            ${allData.pdfs.length === 0 ? 
              '<p class="text-gray-500 col-span-full text-center py-8">Belum ada buku digital</p>' :
              allData.pdfs.map(pdf => `
                <div class="p-4 border rounded-lg hover:shadow-md transition">
                  <div class="flex items-start gap-3">
                    <div class="w-12 h-16 bg-red-100 rounded flex items-center justify-center text-red-500 flex-shrink-0">
                      ${getIcon('file', 'w-6 h-6')}
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="font-medium text-gray-800 truncate">${pdf.pdfTitle}</p>
                      <button onclick="readPdf('${pdf.__backendId}')" class="text-blue-600 text-sm hover:underline mt-2">Baca Buku</button>
                      ${isAdmin ? `<button onclick="confirmDelete('pdf', '${pdf.__backendId}')" class="text-red-500 text-sm hover:underline mt-2 ml-3">Hapus</button>` : ''}
                    </div>
                  </div>
                </div>
              `).join('')
            }
          </div>
        </div>
      `;
    }

    function showPdfUploadModal() {
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'pdfUploadModal';
      modal.innerHTML = `
        <div class="modal-content p-6">
          <h2 class="text-xl font-bold mb-6">Import PDF dari Perangkat</h2>
          <form id="pdfUploadForm" onsubmit="uploadPdfFromDevice(event)">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Judul Buku</label>
                <input type="text" name="pdfTitle" class="input-field" placeholder="Masukkan judul buku" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">File PDF</label>
                <input type="file" accept="application/pdf" onchange="previewPdfFile(event)" class="input-field" required>
                <input type="hidden" name="pdfData" id="pdfDataBase64">
                <div id="pdfFilePreview" class="mt-2"></div>
                <p class="text-xs text-gray-500 mt-1">Upload file PDF dari perangkat Anda (maks. 5MB)</p>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button type="submit" class="btn-primary flex-1">Upload PDF</button>
              <button type="button" onclick="closeModal('pdfUploadModal')" class="btn-secondary">Batal</button>
            </div>
          </form>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    function previewPdfFile(e) {
      const file = e.target.files[0];
      if (!file) return;
      
      if (file.size > 5 * 1024 * 1024) {
        showToast('Ukuran file maksimal 5MB', 'error');
        e.target.value = '';
        return;
      }
      
      const reader = new FileReader();
      reader.onload = function(event) {
        const base64 = event.target.result;
        document.getElementById('pdfDataBase64').value = base64;
        document.getElementById('pdfFilePreview').innerHTML = `
          <div class="flex items-center gap-3 p-3 bg-red-50 rounded-lg">
            <div class="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center">
              ${getIcon('file', 'w-5 h-5 text-red-600')}
            </div>
            <div class="flex-1">
              <p class="text-sm font-medium text-gray-800">${file.name}</p>
              <p class="text-xs text-gray-500">${(file.size / 1024 / 1024).toFixed(2)} MB</p>
            </div>
            <span class="text-green-600 text-xs">✓ Siap diupload</span>
          </div>
        `;
      };
      reader.readAsDataURL(file);
    }

    async function uploadPdfFromDevice(e) {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      
      if (allData.pdfs.length >= 999) {
        showToast('Batas maksimal 999 PDF tercapai', 'error');
        return;
      }
      
      const base64Data = formData.get('pdfData');
      
      if (!base64Data) {
        showToast('Silakan upload file PDF terlebih dahulu', 'error');
        return;
      }
      
      const pdfData = {
        type: 'pdf',
        pdfTitle: formData.get('pdfTitle'),
        pdfData: base64Data
      };
      
      const result = await window.dataSdk.create(pdfData);
      if (result.isOk) {
        showToast('PDF berhasil diupload');
        closeModal('pdfUploadModal');
      } else {
        showToast('Gagal mengupload PDF', 'error');
      }
    }

    function readPdf(pdfId) {
      const pdf = allData.pdfs.find(p => p.__backendId === pdfId);
      if (!pdf || !pdf.pdfData) {
        showToast('PDF tidak ditemukan', 'error');
        return;
      }
      
      const newWindow = window.open('', '_blank');
      newWindow.document.write(`
        <html>
          <head><title>${pdf.pdfTitle}</title></head>
          <body style="margin:0;padding:0;">
            <iframe src="${pdf.pdfData}" style="width:100%;height:100vh;border:none;"></iframe>
          </body>
        </html>
      `);
    }

    // ==================== MUSIC ====================
    let currentPlayingId = null;

    function renderMusic() {
      const content = document.getElementById('contentArea');
      
      content.innerHTML = `
        <div class="card p-6 mb-6">
          <div class="flex flex-wrap gap-4 items-center justify-between mb-6">
            <h3 class="text-lg font-bold text-gray-800">Koleksi Musik Perpustakaan</h3>
            <button onclick="showMusicModal()" class="btn-primary flex items-center gap-2">
              ${getIcon('plus', 'w-5 h-5')} Tambah Musik MP3
            </button>
          </div>
          
          <div class="space-y-3">
            ${allData.music.length === 0 ? 
              '<p class="text-gray-500 text-center py-8">Belum ada musik</p>' :
              allData.music.map(music => `
                <div class="p-4 border rounded-lg hover:bg-gray-50">
                  <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-4">
                      <div class="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center text-purple-600">
                        ${getIcon('music', 'w-6 h-6')}
                      </div>
                      <div>
                        <p class="font-medium text-gray-800">${music.musicTitle}</p>
                        <p class="text-sm text-gray-500">File MP3</p>
                      </div>
                    </div>
                    <div class="flex gap-2">
                      <button onclick="togglePlayMusic('${music.__backendId}')" id="btn-${music.__backendId}" class="p-2 hover:bg-gray-200 rounded-full" title="Putar">
                        ${getIcon('play', 'w-6 h-6 text-green-600')}
                      </button>
                      <button onclick="confirmDelete('music', '${music.__backendId}')" class="p-2 hover:bg-gray-200 rounded-full" title="Hapus">
                        ${getIcon('trash', 'w-6 h-6 text-red-600')}
                      </button>
                    </div>
                  </div>
                  <div id="player-${music.__backendId}" class="hidden mt-3"></div>
                </div>
              `).join('')
            }
          </div>
        </div>
      `;
    }

    function showMusicModal() {
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'musicModal';
      modal.innerHTML = `
        <div class="modal-content p-6">
          <h2 class="text-xl font-bold mb-6">Tambah Musik dari Perangkat</h2>
          <form id="musicForm" onsubmit="saveMusic(event)">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Judul Lagu</label>
                <input type="text" name="musicTitle" class="input-field" placeholder="Masukkan judul lagu" required>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">File MP3</label>
                <input type="file" accept="audio/mp3,audio/mpeg" onchange="previewMusic(event)" class="input-field" required>
                <input type="hidden" name="musicData" id="musicDataBase64">
                <div id="musicPreview" class="mt-2"></div>
                <p class="text-xs text-gray-500 mt-1">Upload file MP3 dari perangkat Anda (maks. 10MB)</p>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button type="submit" class="btn-primary flex-1">Tambah Musik</button>
              <button type="button" onclick="closeModal('musicModal')" class="btn-secondary">Batal</button>
            </div>
          </form>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    async function saveMusic(e) {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      
      if (allData.music.length >= 999) {
        showToast('Batas maksimal 999 lagu tercapai', 'error');
        return;
      }
      
      const musicData = formData.get('musicData');
      
      if (!musicData) {
        showToast('Silakan upload file MP3 terlebih dahulu', 'error');
        return;
      }
      
      const musicDataObj = {
        type: 'music',
        musicTitle: formData.get('musicTitle'),
        musicData: musicData
      };
      
      const result = await window.dataSdk.create(musicDataObj);
      if (result.isOk) {
        showToast('Musik berhasil ditambahkan');
        closeModal('musicModal');
      } else {
        showToast('Gagal menambahkan musik', 'error');
      }
    }

    function togglePlayMusic(musicId) {
      const music = allData.music.find(m => m.__backendId === musicId);
      if (!music || !music.musicData) {
        showToast('Musik tidak ditemukan', 'error');
        return;
      }
      
      const playerContainer = document.getElementById(`player-${musicId}`);
      const btnEl = document.getElementById(`btn-${musicId}`);
      
      // If same music is playing, hide player
      if (currentPlayingId === musicId) {
        playerContainer.classList.add('hidden');
        playerContainer.innerHTML = '';
        currentPlayingId = null;
        btnEl.innerHTML = getIcon('play', 'w-6 h-6 text-green-600');
        btnEl.title = 'Putar';
        return;
      }
      
      // Hide any currently playing music
      if (currentPlayingId) {
        const prevPlayer = document.getElementById(`player-${currentPlayingId}`);
        const prevBtn = document.getElementById(`btn-${currentPlayingId}`);
        if (prevPlayer) {
          prevPlayer.classList.add('hidden');
          prevPlayer.innerHTML = '';
        }
        if (prevBtn) {
          prevBtn.innerHTML = getIcon('play', 'w-6 h-6 text-green-600');
          prevBtn.title = 'Putar';
        }
      }
      
      // Show audio player
      currentPlayingId = musicId;
      playerContainer.innerHTML = `
        <div class="relative bg-gradient-to-r from-purple-50 to-pink-50 p-4 rounded-lg border-2 border-purple-200">
          <audio controls autoplay class="w-full" onended="handleMusicEnded('${musicId}')">
            <source src="${music.musicData}" type="audio/mpeg">
            Browser Anda tidak mendukung pemutar audio.
          </audio>
          <p class="text-sm text-gray-600 mt-2 flex items-center gap-2">
            ${getIcon('music', 'w-4 h-4 text-purple-500')}
            <span>Memutar: <strong>${music.musicTitle}</strong></span>
          </p>
        </div>
      `;
      playerContainer.classList.remove('hidden');
      btnEl.innerHTML = getIcon('pause', 'w-6 h-6 text-red-600');
      btnEl.title = 'Sembunyikan';
      showToast('Memutar: ' + music.musicTitle, 'info');
    }
    
    function handleMusicEnded(musicId) {
      const playerContainer = document.getElementById(`player-${musicId}`);
      const btnEl = document.getElementById(`btn-${musicId}`);
      
      if (playerContainer) {
        playerContainer.classList.add('hidden');
        playerContainer.innerHTML = '';
      }
      
      if (btnEl) {
        btnEl.innerHTML = getIcon('play', 'w-6 h-6 text-green-600');
        btnEl.title = 'Putar';
      }
      
      currentPlayingId = null;
    }

    // ==================== DELETE CONFIRMATION ====================
    function confirmDelete(type, id) {
      const modal = document.createElement('div');
      modal.className = 'modal-overlay';
      modal.id = 'deleteModal';
      modal.innerHTML = `
        <div class="modal-content p-6 max-w-sm">
          <h2 class="text-xl font-bold mb-4 text-red-600">Konfirmasi Hapus</h2>
          <p class="text-gray-600 mb-6">Apakah Anda yakin ingin menghapus data ini? Tindakan ini tidak dapat dibatalkan.</p>
          <div class="flex gap-3">
            <button onclick="executeDelete('${type}', '${id}')" class="btn-danger flex-1">Ya, Hapus</button>
            <button onclick="closeModal('deleteModal')" class="btn-secondary">Batal</button>
          </div>
        </div>
      `;
      document.getElementById('modalContainer').appendChild(modal);
    }

    async function executeDelete(type, id) {
      let dataArray, item;
      
      switch(type) {
        case 'book':
          item = allData.books.find(b => b.__backendId === id);
          break;
        case 'member':
          item = allData.members.find(m => m.__backendId === id);
          break;
        case 'income':
          item = allData.income.find(i => i.__backendId === id);
          break;
        case 'expense':
          item = allData.expenses.find(e => e.__backendId === id);
          break;
        case 'pdf':
          item = allData.pdfs.find(p => p.__backendId === id);
          break;
        case 'music':
          item = allData.music.find(m => m.__backendId === id);
          // Clean up player if this music is being deleted
          if (currentPlayingId === id) {
            const playerContainer = document.getElementById(`player-${id}`);
            if (playerContainer) {
              playerContainer.classList.add('hidden');
              playerContainer.innerHTML = '';
            }
            currentPlayingId = null;
          }
          break;
      }
      
      if (item) {
        const result = await window.dataSdk.delete(item);
        if (result.isOk) {
          showToast('Data berhasil dihapus');
        } else {
          showToast('Gagal menghapus data', 'error');
        }
      }
      
      closeModal('deleteModal');
    }

    function closeModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) modal.remove();
    }

    // ==================== ELEMENT SDK ====================
    if (window.elementSdk) {
      window.elementSdk.init({
        defaultConfig,
        onConfigChange: async (newConfig) => {
          config = { ...config, ...newConfig };
          const titleEl = document.getElementById('appTitle');
          if (titleEl && config.app_title) {
            titleEl.textContent = config.app_title;
          }
        },
        mapToCapabilities: (cfg) => ({
          recolorables: [],
          borderables: [],
          fontEditable: undefined,
          fontSizeable: undefined
        }),
        mapToEditPanelValues: (cfg) => new Map([
          ['app_title', cfg.app_title || defaultConfig.app_title]
        ])
      });
    }

    // ==================== INITIALIZATION ====================
    async function init() {
      // Initialize Data SDK
      if (window.dataSdk) {
        const result = await window.dataSdk.init(dataHandler);
        if (!result.isOk) {
          console.error('Failed to initialize Data SDK');
        }
      }
      
      // Start live time
      updateLiveTime();
      setInterval(updateLiveTime, 1000);
    }

    init();
  </script>
 <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9c14c3b5b003a5cf',t:'MTc2ODk3NzA0My4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
