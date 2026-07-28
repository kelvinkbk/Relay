import os

def write_svg(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def icon_wrapper(paths, filled=False):
    fill = "currentColor" if filled else "none"
    stroke = "none" if filled else "currentColor"
    stroke_width = "0" if filled else "2"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <g fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round">
    {paths}
  </g>
</svg>"""

def generate_navigation():
    os.makedirs('branding/navigation', exist_ok=True)
    
    icons = {
        'chats': '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
        'contacts': '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
        'calls': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
        'saved': '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
        'archive': '<polyline points="21 8 21 21 3 21 3 8"/><rect x="1" y="3" width="22" height="5"/><line x1="10" y1="12" x2="14" y2="12"/>',
        'settings': '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
        'profile': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/>',
        'search': '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
        'new-chat': '<path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>',
        'more': '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>'
    }

    for name, path in icons.items():
        # Default (Outline)
        write_svg(f"branding/navigation/{name}-default.svg", icon_wrapper(path, filled=False))
        # Active (Filled or thicker)
        write_svg(f"branding/navigation/{name}-active.svg", icon_wrapper(path, filled=True))
        # Hover (Same as Default but might have a different class/layer in actual implementation, here just duplicate)
        write_svg(f"branding/navigation/{name}-hover.svg", icon_wrapper(path, filled=False))

def generate_actions():
    os.makedirs('branding/actions', exist_ok=True)
    
    icons = {
        'attach': '<path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>',
        'emoji': '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>',
        'sticker': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/>',
        'gif': '<rect x="3" y="6" width="18" height="12" rx="2"/><text x="12" y="15" font-size="7" font-weight="bold" text-anchor="middle" font-family="sans-serif">GIF</text>',
        'send': '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>',
        'microphone': '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>',
        'reply': '<polyline points="9 17 4 12 9 7"/><path d="M20 18v-2a4 4 0 0 0-4-4H4"/>',
        'forward': '<polyline points="15 17 20 12 15 7"/><path d="M4 18v-2a4 4 0 0 1 4-4h12"/>',
        'edit': '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>',
        'delete': '<polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><line x1="10" y1="11" x2="10" y2="17"/><line x1="14" y1="11" x2="14" y2="17"/>',
        'copy': '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
        'react': '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
        'voice-call': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
        'video-call': '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>',
        'info': '<circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>'
    }

    # Add shared actions (Search, More)
    icons['search'] = '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'
    icons['more'] = '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>'

    for name, path in icons.items():
        write_svg(f"branding/actions/{name}.svg", icon_wrapper(path, filled=False))


def generate_status():
    os.makedirs('branding/status', exist_ok=True)
    
    icons = {
        'online': '<circle cx="12" cy="12" r="6" fill="currentColor"/>',
        'unread': '<circle cx="12" cy="12" r="6" fill="currentColor"/>',
        'muted': '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/>',
        'pinned': '<line x1="12" y1="17" x2="12" y2="22"/><path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a2 2 0 0 0 0-4H8a2 2 0 0 0 0 4h1v4.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24Z"/>',
        'verified': '<path d="M21 12l-1.63-2.77L19.74 6l-3.15-.39L14.77 3l-2.77 1.63L9.23 3 7.4 5.61 4.26 6l.37 3.23L3 12l1.63 2.77L4.26 18l3.15.39L9.23 21l2.77-1.63L14.77 21l1.83-2.61 3.15-.39-.37-3.23L21 12z" stroke="currentColor" fill="currentColor" stroke-width="2"/><polyline points="9 12 11 14 15 10" stroke="#FFF" fill="none" stroke-width="2"/>',
        'sending': '<circle cx="12" cy="12" r="10" stroke-dasharray="8 4" stroke="currentColor" fill="none"/>',
        'sent': '<polyline points="20 6 9 17 4 12" stroke="currentColor" fill="none" stroke-width="2"/>',
        'delivered': '<polyline points="18 6 7 17 2 12" stroke="currentColor" fill="none" stroke-width="2"/><path d="M22 6L11 17l-1.5-1.5" stroke="currentColor" fill="none" stroke-width="2"/>',
        'read': '<polyline points="18 6 7 17 2 12" stroke="currentColor" fill="none" stroke-width="2"/><path d="M22 6L11 17l-1.5-1.5" stroke="currentColor" fill="none" stroke-width="2"/>', # Color differentiation in UI
        'failed': '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
        'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
        'upload': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>'
    }

    for name, path in icons.items():
        write_svg(f"branding/status/{name}.svg", icon_wrapper(path, filled=False))

def generate_tray():
    os.makedirs('branding/tray', exist_ok=True)
    
    # Tiny 16x16 optimized versions of the Relay abstract R
    tray_content = """<circle cx="4" cy="4" r="1.5" fill="currentColor"/><circle cx="4" cy="12" r="1.5" fill="currentColor"/><path d="M4 4 L 10 4 A 3 3 0 0 1 10 10 L 4 10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M 8 10 L 12 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>"""
    
    tray_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">{tray_content}</svg>"""
    
    write_svg("branding/tray/relay-tray-dark.svg", tray_svg)
    write_svg("branding/tray/relay-tray-light.svg", tray_svg)
    
    tray_unread_content = tray_content + '<circle cx="12" cy="4" r="2" fill="#EF4444"/>'
    tray_unread_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">{tray_unread_content}</svg>"""
    write_svg("branding/tray/relay-tray-unread.svg", tray_unread_svg)

def generate_special():
    os.makedirs('branding/onboarding', exist_ok=True)
    os.makedirs('branding/installer', exist_ok=True)
    
    # Just copying the lockup or symbol to these for completeness of the asset package
    import shutil
    try:
        shutil.copy("branding/logo/relay-lockup.svg", "branding/onboarding/relay-onboarding-logo.svg")
        shutil.copy("branding/logo/relay-lockup.svg", "branding/installer/relay-installer-header.svg")
        shutil.copy("branding/logo/relay-symbol-mono.svg", "branding/status/relay-notification-mark.svg")
    except Exception as e:
        print("Error copying special assets:", e)

if __name__ == "__main__":
    generate_navigation()
    generate_actions()
    generate_status()
    generate_tray()
    generate_special()
    print("All UI icons generated.")
