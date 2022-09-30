from fastapi import APIRouter

from app.api.api_v1.endpoints import pay_terminal

api_router = APIRouter()
# api_router.include_router(auth.router, prefix="/auth", tags=["Auth (Авторизация)"])
# api_router.include_router(organization.router, prefix="/organizations", tags=["Organization (Организации ТОР)"])
# api_router.include_router(receipt.router, prefix="/receipts", tags=["Receipts (Квитанции)"])
# api_router.include_router(handler_1c_enterprise.router, prefix="/1c_enterprise", tags=["Enterprise 1C (1C Предпиятие)"])
# api_router.include_router(handler_erip.router, prefix="", tags=["ERIP (ЕРИП)"])
api_router.include_router(pay_terminal.router, prefix="/pay_terminal", tags=["Pay terminals (Терминалы)"])
