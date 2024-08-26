from shiny import ui, render, App
from calculator import Calculation as calc
from pathlib import Path

def abs_panel(right:str, top:str, info:str):
    return ui.panel_absolute(ui.panel_well(info),
                        width="300px", 
                        draggable=True,  
                        )

# <iframe src="https://trinket.io/embed/python/a868a718f9" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

app_ui = ui.page_fixed(
    ui.navset_tab(   
        ui.nav_panel("A", 
                     ui.page_sidebar(  
                     ui.sidebar(ui.card(ui.input_text("txt_in", "Type something here:")),
                                ui.card(ui.input_select('var1', 'Choose a figure', choices=['Figure 1', 'Figure 2'])), 
                                ui.card(ui.panel_title("Save vs  Pay test 123!"),
                                        ui.h3("Loan details"),
                                        ui.input_slider("ln_r", "Loan interest rate", 0.1, 10.0, 3.5),
                                        ui.input_slider("tenure", "Loan tenure", 0.1, 35.0, 10.0),
                                        ui.input_numeric("loan_amt", label="Enter loan amount", value=100000),
                                        ui.h3("Investment details"),
                                        ui.input_slider("fv_r", "Investment interest rate", 0.1, 10.0, 3.5),
                                        ui.h3("Other details"),
                                        ui.input_numeric("every_rm", label="Enter every rm", value=100),
                                        ui.input_numeric("until_rm", label="Enter until rm", value=1000)),
                                bg="#f8f8f8", width=350),  
                        ui.h2("Main content"), 
                        ui.card(ui.output_code("results"), 
                        ui.card(ui.h4('Figure'), ui.output_plot("hist1")),
                        ui.card(ui.output_data_frame("repay_table"),)) 
)  ,                     
),
        ui.nav_panel("B", 
                    abs_panel('50px', '50px', 'Slower growth in trade partners'),
                    abs_panel('60px', '60px', 'Further tightening of domestic lending standards'), 
                    abs_panel('60px', '60px', 'External funds more expensive (counterparty, credit risks, parent bank problems)'), 
                    abs_panel('60px', '60px', 'Tightening of domestic lending standards'), 
                    abs_panel('60px', '60px', 'Reduced lending and/or reduced loan demand of domestic households and firms'), 
                    abs_panel('60px', '60px', 'Reduced domestic consumption and investment spending'), 
                    abs_panel('60px', '60px', 'Slowdown in domestic economy'), 
                    abs_panel('60px', '60px', 'Domestic borrower debt service problems /declining asset quality'), 
                    # ui.panel_absolute('hello',
                    #     width="200px",  
                    #     draggable=True,), 
                    ui.output_image('image_1')    
    
                    
    ),
        ui.nav_panel("C", 
                     ui.h2('Embedded Python Code Editor'), 
                     ui.p(ui.br(), 'Using ', ui.tags.b('Trinket'), ' we can embed python code editor into the web app'),
                     ui.tags.iframe(src="https://trinket.io/embed/python/a868a718f9", width="100%", height="356", frameborder="0", marginwidth="0")),
        id="tab",  
    )  

)

def server(input, output, session):
    @render.code
    def results():
        if input.txt_in() == "":
            return "This web app is build using Shiny (Python).\nThe core of Shiny revolves around the concept of reactive programming, \
                    where changes in inputs\n(such as sliders or buttons) trigger automatic updates in outputs (such as plots or tables)."
        return f"You entered '{input.txt_in()}'."
    
    @render.data_frame
    def repay_table():
        x = calc(loan_interest=(input.ln_r())/100,loan_amount=input.loan_amt(), ln_tenure=input.tenure(), fv_interest_rate=(input.fv_r())/100, every_rm = input.every_rm(), until_rm = input.until_rm())
        df, fig = x.compile()
        return render.DataGrid(df.applymap(lambda x: f"{x:,.2f}"), selection_mode="rows")
    
    @render.plot
    def hist1(): 
        x = calc(loan_interest=(input.ln_r())/100,loan_amount=input.loan_amt(), ln_tenure=input.tenure(), fv_interest_rate=(input.fv_r())/100, every_rm = input.every_rm(), until_rm = input.until_rm())
        df, fig1= x.compile()
        fig2 = df[['value']].plot(kind='bar', title=f'value on every RM{input.every_rm()}').set_ylabel('in RM')
        # print(str(input.var1)) -- <shiny.reactive._reactives.Value object at 0x0000011F81491970>
        if str(input.var1()) == "Figure 1":
            return fig1
        else:            
            return fig2
    
    @render.image
    def image_1():
        path = Path(__file__).parent
        img = {"src": path / 'Session 10 Group Work Slides Roger.jpg', 'width': '100%'}
        return img


app = App(app_ui, server)