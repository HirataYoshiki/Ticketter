from fastapi import APIRouter, Depends
from apps.Interactions import Controls
from apps.Interactions import Schemes

router = APIRouter()

@router.post('/interactions')
async def give_tickets(interactions = Depends(Controls.give_tickets)):
  return interactions

@router.delete('/interactions')
async def delete_my_given_tickets(deletes = Depends(Controls.delete_my_given_tickets)):
  return deletes

@router.post('/interactions/{uid}')
async def give_a_ticket(interaction: Schemes.TicketInteractionOut = Depends(Controls.give_a_ticket)):
  return interaction

@router.get('/interactions/{uid}')
async def get_interactions_of_the_user(
  selections: list = Depends(Controls.get_interactions)
):
  return selections