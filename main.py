import flet as ft
import base64
import time
import threading
from datetime import datetime

def main(page: ft.Page):
    
    page.title = "Biswajeet Portfolio"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = "auto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    def update_front_section(e):
        front_text.size = 30 if page.window.width < 768 else 70
        front_section.height = 500 if page.window.width < 768 else 700
        page.update()

    with open("./assets/images/myimage.jpg", "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    
    with open("./assets/images/home-bg.jpg", "rb") as image_file:
        base64_image_hbg = base64.b64encode(image_file.read()).decode("utf-8")
    
    with open("./assets/images/one.png", "rb") as image_file:
        one_image = base64.b64encode(image_file.read()).decode("utf-8")
        
    with open("./assets/images/two.png", "rb") as image_file:
        two_image = base64.b64encode(image_file.read()).decode("utf-8")
        
    with open("./assets/images/three.png", "rb") as image_file:
        three_image = base64.b64encode(image_file.read()).decode("utf-8")
        
    with open("./assets/images/four.png", "rb") as image_file:
        four_image = base64.b64encode(image_file.read()).decode("utf-8")
        
    with open("./assets/images/five.png", "rb") as image_file:
        five_image = base64.b64encode(image_file.read()).decode("utf-8")
        
    with open("./assets/images/six.png", "rb") as image_file:
        six_image = base64.b64encode(image_file.read()).decode("utf-8")
    
    
    full_text = "This website is fully developed by me in Python FLET. To know more about FLET Python, visit 'https://flet.dev/'"
    sub_text = ft.Text("", 
        size="20", 
        color=ft.colors.ON_SURFACE,
        opacity=0.6,
    )
    animated_text_container = ft.AnimatedSwitcher(
        sub_text,
        duration=300,
        transition=ft.AnimatedSwitcherTransition.FADE,
        width=510
    )
    def typing_animation():
        current_text = ""
        for char in full_text:
            current_text += char
            sub_text.value = current_text
            page.update()
            time.sleep(0.05)
        threading.Timer(5, typing_animation).start()
    threading.Thread(target=typing_animation).start()
    
    
    title_text = "Welcome to Playground"
    front_text = ft.Text(
        "",
        size=60,
        weight="bold",
        color=ft.colors.ON_SURFACE,
        text_align=ft.TextAlign.CENTER,
        opacity=0.8
    )
    
    animated_title_text = ft.AnimatedSwitcher(
        front_text,
        duration=300,
        transition=ft.AnimatedSwitcherTransition.FADE,
    )
    def title_animation():
        current_text = ""
        for char in title_text:
            current_text += char
            front_text.value = current_text
            page.update()
            time.sleep(0.05)
        threading.Timer(7, title_animation).start()
    threading.Thread(target=title_animation).start()
    
    front_section = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Column(
                    [
                        ft.Container(
                            content=animated_title_text,
                            col={"xs": 12, "sm": 10, "md": 8, "lg": 6},
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=animated_text_container,
                            col={"xs": 12, "sm": 10, "md": 8, "lg": 6},
                            alignment=ft.alignment.center,
                        ),
                        
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        image_src_base64=base64_image_hbg,
        image_fit=ft.ImageFit.COVER,
        image_opacity=0.5,
        alignment=ft.alignment.center,
        height=700 if page.window.width < 768 else 700,
    )
    
    page.on_resized = update_front_section
    
    profile_image = ft.Container(
        content=ft.Image(
            src_base64=base64_image,
            width=210,
            height=230,
            fit=ft.ImageFit.CONTAIN
        ),
        col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
        alignment=ft.alignment.center,
    )
    
    profile_card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Biswajeet Behera", size=30, weight="bold", color=ft.colors.ON_SURFACE),
                ft.Text("biswajeetbehera.off@gmail.com", size=15, color=ft.colors.ON_SURFACE),
                ft.Text("+91-8114727162", size=15, color=ft.colors.ON_SURFACE),
                ft.Text("Centurion University of Technology and Management, Paralakhemundi, Odisha", size=15, color=ft.colors.ON_SURFACE),
                
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text("LinkedIn:", color=ft.colors.ON_SURFACE),
                                    ft.Text("linkedin.com/in/biswajeetbehera-off", color=ft.colors.PRIMARY),
                                ],
                                spacing=5
                            ),
                            col={"xs": 12, "sm": 6},
                            url="http://www.linkedin.com/in/biswajeetbehera-off"
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text("GitHub:", color=ft.colors.ON_SURFACE),
                                    ft.Text("Github.com/Biswajeet-Behera-off", color=ft.colors.PRIMARY),
                                ],
                                spacing=5
                            ),
                            col={"xs": 12, "sm": 6},
                            url="https://github.com/Biswajeet-Behera-off"
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.OutlinedButton(
                                "View more projects",
                                width=200,
                                height=50,
                                url="https://github.com/Biswajeet-Behera-off",
                                
                            ),
                            col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                        ),
                        ft.Container(
                            ft.OutlinedButton(
                                "Download my CV",
                                url="https://drive.google.com/file/d/1zfOmF5b9v82SLQgjCqTlxPgn5p-hdW6E/view?usp=sharing",
                                width=180,
                                height=50
                            ),
                            col={"xs": 12, "sm": 6, "md": 4, "lg": 3}
                        ),
                    ]
                )
            ],
            spacing=10,
        ),
        col={"xs": 12, "sm": 12, "md": 8, "lg": 9},
    )
    

    profile_section = ft.Container(
        content=ft.ResponsiveRow(
            [
                profile_image, 
                profile_card
            ],
            alignment=ft.MainAxisAlignment.START,  # Align items to the start of the row
        ),
        border=ft.border.all(3,color=ft.colors.AMBER),
        padding=20
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
                            ft.Image(src_base64=one_image, width=700, height=200, fit=ft.ImageFit.CONTAIN),
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
                            ft.Image(src_base64=two_image, width=700, height=200, fit=ft.ImageFit.CONTAIN),
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
                            ft.Image(src_base64=three_image, width=700, height=200, fit=ft.ImageFit.CONTAIN),
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
                            ft.Image(src_base64=four_image, width=700, height=200, fit=ft.ImageFit.CONTAIN),
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
                            ft.Image(src_base64=five_image, width=700, height=200, fit=ft.ImageFit.CONTAIN),
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
                            ft.Image(src_base64=six_image, width=700, height=200, fit=ft.ImageFit.CONTAIN),
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
            ]
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
        bgcolor="#848d9c",
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
    
    
    page.add(
        ft.Column(
            [
                front_section,
                profile_section,
                ft.Container(
                    content=skills_card,
                    alignment=ft.alignment.center,
                    margin=ft.Margin(0,20,0,0)
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            project,
                            padding=20
                        ) for project in project_cards
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
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
            expand=True
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
