# Relay Design System

This document outlines the core visual language and design tokens for Relay.

## Brand Identity

Relay is the native communication and messaging application for TheonixOS. The brand communicates Connection, Speed, Flow, Trust, Modern technology, and Human interaction.

### Typography
- **Font Family**: Inter / Native OS Font
- **Weights**: Regular (400), Semibold (600)

### Color Palette

The color system is built around Indigo and Violet, designed to feel premium and state of the art.

#### Primary Brand Colors
- **Primary Indigo**: `#6366F1` (Used for active states, primary buttons, active chat backgrounds, active navigation indicator)
- **Accent Violet**: `#8B5CF6` (Used for highlights, hover states, active text)

#### Light Theme Neutrals (colors.palette)
- **Background**: `#FFFFFF`
- **Surface Hover**: `#F5F6F8`
- **Surface Active/Ripple**: `#EBEDF0`

#### Dark Theme Neutrals (night.tdesktop-theme)
- **Background**: `#1A1A1D`
- **Surface Hover**: `#222225`
- **Surface Active/Ripple**: `#2A2A2D`

## Geometry & Radii

Relay relies on soft, rounded corners to create a modern, approachable interface.

- **`relayRadius`**: 12px (Standard component radius for panels, standard message bubbles)
- **`relayMessageRadius`**: 16px (Large standalone message bubbles)
- **`relayInputRadius`**: 16px (Composer input field)
- **`buttonRadius`**: 8px (Action buttons, login buttons)
- **`boxRadius`**: 16px (Modals, popup boxes, context menus)
- **`relayPanelRadius`**: 12px (Navigation active indicators, floating panels)

## Elevation & Surfaces

- **Navigation Rail**: Persistent 70px wide rail on the left.
- **Active States**: High contrast primary color (`#6366F1`) with white text/icons.
- **Hover States**: Subtle shifts in background lightness (e.g. `windowBgOver`).

## States Mapping

| State | Background Color | Text/Icon Color |
|-------|------------------|-----------------|
| Default | `windowBg` | `windowFg` / `menuIconFg` |
| Hover | `windowBgOver` | `windowFgOver` / `menuIconFg` |
| Active | `#6366F1` | `#FFFFFF` (`windowFgActive`) |
| Active Hover | `#8B5CF6` | `#FFFFFF` |

## Usage Guidelines

1. **Brand Colors**: Use `#6366F1` and `#8B5CF6` strictly for interactive/semantic states (Selection, Primary actions, Focus, Unread emphasis). Avoid flooding the UI with these colors.
2. **Icons**: Navigation icons should use `windowFgActive` when selected to contrast against the Indigo background.
3. **Empty States**: Background should use the generated subtle cool gradient (`bg_initial.jpg`).
