from aiogram import Router

from .handlers import (add, admin, description, edit, extension, home,
                       instruction, remove, settings, start, subscribe,
                       subscription)
from .services import form_payment

router = Router()
router.include_router(start.router)
router.include_router(admin.router)
router.include_router(home.router)

router.include_router(description.router)
router.include_router(instruction.router)
router.include_router(subscribe.router)
router.include_router(subscription.router)
router.include_router(extension.router)
router.include_router(settings.router)
router.include_router(edit.router)
router.include_router(add.router)
router.include_router(remove.router)

router.include_router(form_payment.router)
