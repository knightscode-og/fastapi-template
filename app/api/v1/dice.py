from fastapi import APIRouter, HTTPException
from typing import List, Tuple
from app.controllers.dice import roll_dice

router = APIRouter()

@router.post("/roll")
async def roll_dice_route(dice: List[Tuple[int, int]]):
    """
    Endpoint to roll multiple dice.
    
    Args:
        dice (List[Tuple[int, int]]): A list of tuples where each tuple contains the number of dice and the type of dice.
                                      For example, [(1, 8), (3, 4)] represents 1d8 and 3d4.
    
    Returns:
        Dict[str, Any]: A dictionary with the detailed results for each dice roll and the total.
    """
    try:
        results = roll_dice(dice)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))