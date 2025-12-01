
# Shared CSS Styles

GLOBAL_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --primary: #2ecc71;
        --primary-light: #e8f8f5;
        --text-dark: #2c3e50;
        --text-gray: #7f8c8d;
        --bg-color: #f8f9fa;
        --card-bg: #ffffff;
        --danger: #e74c3c;
        --warning: #f1c40f;
        --success: #27ae60;
        --info: #3498db;
    }

    .dashboard-container {
        font-family: 'Inter', sans-serif;
        background-color: var(--bg-color);
        padding: 20px;
        border-radius: 12px;
        color: var(--text-dark);
        max-width: 1200px;
        margin: 0 auto;
        min-height: 800px;
    }

    /* Header */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 1px solid #eee;
    }
    .brand {
        font-size: 20px;
        font-weight: 700;
        color: var(--text-dark);
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .brand-icon {
        background: var(--primary);
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
    }
    .nav-menu {
        display: flex;
        gap: 20px;
        font-size: 14px;
        color: var(--text-gray);
    }
    .nav-item {
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 6px 12px;
        border-radius: 20px;
        transition: all 0.2s;
    }
    .nav-item:hover {
        background: #f0f0f0;
    }
    .nav-item.active {
        background: #d1f2eb;
        color: var(--success);
        font-weight: 600;
    }

    /* Common Layouts */
    .grid-3 {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-bottom: 20px;
    }
    .grid-2 {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin-bottom: 20px;
    }
    .grid-1-2 {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 20px;
        margin-bottom: 20px;
    }

    /* Cards */
    .card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        border: 1px solid #f0f0f0;
        height: 100%;
        box-sizing: border-box;
        position: relative;
    }
    .card-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--text-dark);
        margin-bottom: 16px;
    }

    /* Buttons */
    .btn {
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        border: none;
        display: flex;
        align-items: center;
        gap: 8px;
        justify-content: center;
        transition: opacity 0.2s;
    }
    .btn:hover {
        opacity: 0.9;
    }
    .btn-primary {
        background: var(--primary);
        color: white;
        box-shadow: 0 2px 6px rgba(46, 204, 113, 0.3);
    }
    .btn-outline {
        background: white;
        border: 1px solid #ddd;
        color: var(--text-dark);
    }
    .btn-full {
        width: 100%;
    }

    /* Typography */
    .text-success { color: var(--success); }
    .text-warning { color: var(--warning); }
    .text-danger { color: var(--danger); }
    .text-gray { color: var(--text-gray); }
    .font-bold { font-weight: 700; }
    
    /* Specific Components */
    .status-badge {
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
    }
    .badge-success { background: #eafaf1; color: var(--success); }
    .badge-warning { background: #fef9e7; color: var(--warning); }
    
</style>
"""
