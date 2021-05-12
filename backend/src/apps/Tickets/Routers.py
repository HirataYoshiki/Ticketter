from typing import List

from fastapi import APIRouter, Depends
from apps.Tickets import Controls
from apps.Tickets import Schemes
router = APIRouter()

@router.post('/tickets', response_model= Schemes.TicketOut)
async def create_ticket(ticket: Schemes.TicketOut = Depends(Controls.create_ticket)):
  return ticket

@router.get('/tickets', response_model = List[Schemes.TicketOut])
async def get_tickets(tickets:list = Depends(Controls.get_tickets)):
  return tickets

@router.get('/tickets/{ticketid}', response_model = Schemes.TicketOut)
async def get_ticket(ticket: Schemes.TicketOut = Depends(Controls.get_ticket)):
  return ticket