import flet as ft
from parallax import parallax_effect
import asyncio
from datetime import datetime


async def main(page: ft.Page):
    
    page.title = "Biswajeet Portfolio"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = "auto"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.padding = 0
    page.bgcolor = "#365563"
    
    
    loading_screen = ft.Container(
    content=ft.Column(
        [
            ft.ProgressRing(color=ft.colors.AMBER_400, scale=1.5),
            ft.Text("Loading portfolio ...", color=ft.colors.AMBER_100, size=20),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ),
    height=page.height,
    width=page.width,
    bgcolor=ft.colors.BLACK,
    alignment=ft.alignment.center,
)
    page.add(ft.Container(
    content=loading_screen,
    alignment=ft.alignment.center,
    expand=True,
    bgcolor=ft.colors.BLACK,
    height=page.height
))
    page.update()

    async def typewriter_effect(page: ft.Page, type_text: ft.Text, animate_text: str):
        while True:
            # Type forward
            for i in range(len(animate_text) + 1):
                type_text.value = animate_text[:i]
                page.update()
                await asyncio.sleep(0.1)

            # Pause at full text
            await asyncio.sleep(1)

            # Erase backward
            for i in range(len(animate_text), -1, -1):
                type_text.value = animate_text[:i]
                page.update()
                await asyncio.sleep(0.05)
    
    async def load_main_content():
        await asyncio.sleep(3)
        
        type_text = ft.Text("",size=24, italic=True, color=ft.colors.LIGHT_BLUE_200, col={"xs": 12, "md": 6, "lg": 3})
        asyncio.create_task(typewriter_effect(page, type_text, "Python Developer | Data Analyst"))
        
        parallax = parallax_effect(900,600)

        front_section = ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Column(
                        controls=[
                            ft.Text("👋 Hello, I'm", size=20, color=ft.colors.GREY,col={"xs": 12, "md": 6, "lg": 3}),
                            type_text,
                            ft.Text("Building clean, insightful, and efficient solutions.", size=16, color=ft.colors.GREY_300, col={"xs": 12, "md": 6, "lg": 3}),
                            ft.Text("This web page customized in Flet library with python.", size=16, color=ft.colors.GREY_300, col={"xs": 12, "md": 6, "lg": 3}),
                            ft.ElevatedButton("Download Resume", icon=ft.icons.FILE_DOWNLOAD, bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE, col={"xs": 12, "md": 6, "lg": 3}),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            image= ft.DecorationImage(src="images/home-bg.jpg", fit=ft.ImageFit.COVER,opacity=0.7),
            
            alignment=ft.alignment.center,
            height=700,
        )
        def update_front_section(e):
            front_section.height = 500 if page.window.width < 768 else 700
            page.update()
        
        page.on_resized = update_front_section
        
        profile_image = ft.Container(
            content=ft.Image(
                src="images/myimage.jpg",
                width=210,
                height=230,
                fit=ft.ImageFit.CONTAIN
            ),
            col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
            alignment=ft.alignment.center,
        )
        
        profile_card = ft.Stack(
            [
                parallax,
                ft.Column(
                    [
                        profile_image,
                        ft.Text("Biswajeet Behera", size=30, weight="bold", color=ft.colors.ON_SURFACE),
                        ft.Text("work.biswajeetbehera@gmail.com", size=15, color=ft.colors.ON_SURFACE),
                        ft.Text("756125, Basudevpur,Bhadrak, Odisha", size=15, color=ft.colors.ON_SURFACE),
                        ft.ResponsiveRow(
                            [
                                ft.Container(
                                    ft.ElevatedButton(
                                        "LinkedIn",
                                        height=50,
                                        url="http://www.linkedin.com/in/biswajeetbehera-off",
                                        style=ft.ButtonStyle(
                                            padding=ft.padding.symmetric(horizontal=20)),
                                    ),
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                                ),
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Github",
                                        height=50,
                                        url="https://github.com/Biswajeet-Behera-off",
                                        style=ft.ButtonStyle(
                                            padding=ft.padding.symmetric(horizontal=20)),
                                    ),
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                                ),
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Instagram",
                                        height=50,
                                        url="https://www.instagram.com/biswajeetbehera.off",
                                        style=ft.ButtonStyle(
                                            padding=ft.padding.symmetric(horizontal=20)),
                                    ),
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            run_spacing=10
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            ],
            alignment=ft.Alignment(0.0, 0.0),
            width=900,
            height=600,
        )


        skills_card = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Skills", size=30, weight="bold", color=ft.colors.ON_SURFACE, text_align=ft.TextAlign.CENTER),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Python", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Pandas", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("EDA", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("ETL", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("SQL", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("EXCEL", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Power Bi", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Dashbording", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Data Analysis", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Data Cleaning", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Data Preparation", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Data Visualization", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Machine Learning", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.ON_SURFACE),
                                        ft.Text("Deep Learning", size=20, weight="bold", color=ft.colors.ON_SURFACE)
                                    ]
                                ),
                                col={"xs": 12, "sm": 6}
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            padding=30,
            width=470,
            border=ft.border.all(3, color=ft.colors.AMBER)
        )
        
        project_cards = [
            ft.ResponsiveRow(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="images/one.png", width=700, height=200, fit=ft.ImageFit.CONTAIN),
                                ft.Text("Lung Cancer Analysis", size=16, weight="bold", color=ft.colors.ON_SURFACE),
                                ft.Text("This project aims to analyze and predict lung cancer patient data using Python and machine-learning techniques.", opacity=0.6,color=ft.colors.ON_SURFACE)
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        border_radius=10,
                        expand=True,
                        url="https://github.com/Biswajeet-Behera-off/lung_cancer_analysis",
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="images/two.png", width=700, height=200, fit=ft.ImageFit.CONTAIN),
                                ft.Text("Restaurant Data Analysis using Power Bi", size=16, weight="bold", color=ft.colors.ON_SURFACE),
                                ft.Text("Data-Driven Insights for a Restaurant Data Analysis. || Learning from Rishabh Mishra . As a Beginner Data analyst, I recently worked in restaurant data analysis.", opacity=0.6,color=ft.colors.ON_SURFACE)
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        border_radius=10,
                        expand=True,
                        url="https://github.com/Biswajeet-Behera-off/Restaurant-data-analysis",
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="images/three.png", width=700, height=200, fit=ft.ImageFit.CONTAIN),
                                ft.Text("HR Analysis Report || Employee attrition trends data analysis", size=16, weight="bold", color=ft.colors.ON_SURFACE),
                                ft.Text("Data-Driven Insights for an HR Analysis. || Learning from Rishabh Mishra, This is my Second Project on Power Bi. As a Beginner Data analyst, I recently worked on employee attrition trends Data analysis.", opacity=0.6,color=ft.colors.ON_SURFACE)
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        border_radius=10,
                        expand=True,
                        url="https://github.com/Biswajeet-Behera-off/HR-Analysis-Report",
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="images/four.png", width=700, height=200, fit=ft.ImageFit.CONTAIN),
                                ft.Text("BB ELECTRONICS SALES DATA ANALYSIS", size=16, weight="bold", color=ft.colors.ON_SURFACE),
                                ft.Text("This project presents an analysis of electrinics sales data based on their two years of store sales using pivot tables and Formula in Excel and visualizing chart for Dashboarding.", opacity=0.6,color=ft.colors.ON_SURFACE)
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        border_radius=10,
                        expand=True,
                        url="https://github.com/Biswajeet-Behera-off/BB_electronics_sales_analysis",
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="images/five.png", width=700, height=200, fit=ft.ImageFit.CONTAIN),
                                ft.Text("Superstore Sales Data Analysis", size=16, weight="bold", color=ft.colors.ON_SURFACE),
                                ft.Text("This project presents an in-depth analysis of the Superstore Sales dataset, which encompasses over 51,000 records detailing customer orders, shipping modes, product categories, and financial metrics, such as sales, discount, profit, and shipping costs", opacity=0.6,color=ft.colors.ON_SURFACE)
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        border_radius=10,
                        expand=True,
                        url="https://github.com/Biswajeet-Behera-off/Superstore_sales_analysis_Power-BI",
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="images/six.png", width=700, height=200, fit=ft.ImageFit.CONTAIN),
                                ft.Text("Walmart Sales Data Analysis", size=16, weight="bold", color=ft.colors.ON_SURFACE),
                                ft.Text("This project involves setting up a Walmart sales database and performing an in-depth analysis to derive insights on sales performance, customer preferences, and product trends. SQL is used extensively for data loading, feature engineering, and analysis.", opacity=0.6,color=ft.colors.ON_SURFACE)
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=10,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        border_radius=10,
                        expand=True,
                        url="https://github.com/Biswajeet-Behera-off/Walmart_sales_data_analysis",
                        col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                    )
                ],
            )
        ]


        def handle_close(e):
            page.close(thank_you_dialog)
        
        thank_you_dialog = ft.AlertDialog(
            content=ft.Text("Thank you! Your message has been sent.", color=ft.colors.BLUE_GREY_700),
            modal=True,
            actions=[ft.TextButton("Close", on_click=handle_close)],
        )
        
        submit_button = ft.ElevatedButton(
            text="Submit",
            width=400,
            height=45,
            bgcolor=ft.colors.BLUE_ACCENT_700,
            color=ft.colors.WHITE,
            on_click=lambda e: page.open(thank_you_dialog)
        )
        
        contact_card = ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            ft.Text("Feedback Form", color=ft.colors.ON_SURFACE, size=30, width="bold", text_align=ft.TextAlign.CENTER),
                            ft.TextField(label="Name", width=600,color=ft.colors.ON_SURFACE, border=ft.border.all(3,color=ft.colors.BLACK12)),
                            ft.TextField(label="Email", width=600,color=ft.colors.ON_SURFACE, border=ft.border.all(3,color=ft.colors.BLACK12)),
                            ft.TextField(label="Subject", width=600,color=ft.colors.ON_SURFACE, border=ft.border.all(3,color=ft.colors.BLACK12)),
                            ft.TextField(label="Message", multiline=True, width=600, height=150,color=ft.colors.ON_SURFACE, border=ft.border.all(3,color=ft.colors.BLACK12)),
                            submit_button
                        ],
                        col={"xs": 12, "sm": 12, "md": 12, "lg": 12},
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8
                    )
                ]
            ),
            padding=20,
            border_radius=8,
            bgcolor=ft.colors.BLUE_GREY_800,
            alignment=ft.alignment.center,
            width=650
        )
        
        current_year = datetime.now().year
        
        footer_card = ft.Container(
            content=ft.Text(
                f"© copyright {current_year} Biswajeet. All rights reserved.",
                text_align= ft.TextAlign.CENTER,
                size=20,
                color=ft.colors.ON_SURFACE,
                opacity=0.4
            ),
        )
        
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    front_section,
                    profile_card,
                    ft.Container(
                        content=skills_card,
                        alignment=ft.alignment.center,
                        margin=ft.Margin(0,20,0,0)
                    ),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                project,
                                padding=20,
                                
                            ) for project in project_cards
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        width=1111
                    ),
                    ft.Container(
                        content=contact_card,
                        alignment=ft.alignment.center,
                        padding=20
                    ),
                    ft.Container(
                        content=footer_card,
                        alignment=ft.alignment.center,
                        expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            )
        )
        page.update()
    try:
        await asyncio.wait_for(load_main_content(), timeout=5)
    except Exception as e:
        print("⚠️ Error while loading content:", e)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
