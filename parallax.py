import flet as ft

def parallax_effect(width, height):
    # Icons configuration with positions
    icons = [
        {"icon": ft.icons.CODE, "color": ft.colors.AMBER_400, "size": 35, "left": 50, "top": 50},
        {"icon": ft.icons.PALETTE, "color": ft.colors.RED_400, "size": 45, "left": 120, "top": 200},
        {"icon": ft.icons.ANDROID, "color": ft.colors.GREEN_400, "size": 55, "left": 80, "top": 400},
        {"icon": ft.icons.APPLE, "color": ft.colors.PURPLE_400, "size": 40, "left": 200, "top": 500},
        {"icon": ft.icons.WIDGETS, "color": ft.colors.CYAN_400, "size": 50, "left": 700, "top": 80},
        {"icon": ft.icons.DATA_OBJECT, "color": ft.colors.AMBER_400, "size": 35, "left": 750, "top": 250},
        {"icon": ft.icons.BRUSH, "color": ft.colors.RED_400, "size": 45, "left": 650, "top": 400},
        {"icon": ft.icons.PHONE_ANDROID, "color": ft.colors.GREEN_400, "size": 40, "left": 400, "top": 150},
        {"icon": ft.icons.LAPTOP_MAC, "color": ft.colors.PURPLE_400, "size": 50, "left": 450, "top": 300},
        {"icon": ft.icons.BUILD, "color": ft.colors.CYAN_400, "size": 60, "left": 380, "top": 450},
        {"icon": ft.icons.CLOUD, "color": ft.colors.BLUE_400, "size": 40, "left": 250, "top": 300},
        {"icon": ft.icons.STORAGE, "color": ft.colors.ORANGE_400, "size": 45, "left": 600, "top": 200},
    ]
    
    offsets = [0.5, 0.55, 0.6, 0.7, 0.55, 0.65, 0.55, 0.6, 0.5, 0.65, 0.55, 0.7]
    icon_containers = []

    # Create all icon containers first
    for icon_data in icons:
        icon_container = ft.Container(
            content=ft.Icon(
                icon_data["icon"],
                color=icon_data["color"],
                size=icon_data["size"]
            ),
            left=icon_data["left"],
            top=icon_data["top"],
            animate_position=100,
            opacity=0.8,
        )
        icon_containers.append(icon_container)

    main_container = ft.Container(
        content=ft.Stack(icon_containers),
        width=width,
        height=height,
        padding=20,
        bgcolor=ft.colors.BLUE_GREY_800,
        border_radius=ft.BorderRadius(15,15,15,15)
    )

    # Hover movement handler
    def on_hover(e: ft.HoverEvent):
        if not e.local_x or not e.local_y:
            return
            
        for i, icon in enumerate(icon_containers):
            movement_x = (e.local_x - 450) * offsets[i] / 5
            movement_y = (e.local_y - 300) * offsets[i] / 5
            
            new_left = icons[i]["left"] + movement_x
            new_top = icons[i]["top"] + movement_y
            
            icon.left = max(0, min(new_left, 900 - icons[i]["size"]))
            icon.top = max(0, min(new_top, 600 - icons[i]["size"]))
        
        main_container.content.update()

    # Retuen with gesture detector
    return ft.GestureDetector(
        content=main_container,
        on_hover=on_hover,
        opacity=0.5,
    )