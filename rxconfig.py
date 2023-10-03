import reflex as rx

class ReflexappConfig(rx.Config):
    pass

config = ReflexappConfig(
    app_name="reflex_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)