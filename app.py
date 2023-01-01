from app.app import OptimizeLifeApp

if __name__.startswith("bokeh_app"):
    life_app = OptimizeLifeApp()
    life_app.servable()
