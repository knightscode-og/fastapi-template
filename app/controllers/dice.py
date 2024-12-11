import random
from typing import List, Tuple, Dict, Any

def roll_dice(dice: List[Tuple[int, int]]) -> Dict[str, Any]:
    """
    Simulate rolling multiple dice.
    
    Args:
        dice (List[Tuple[int, int]]): A list of tuples where each tuple contains the number of dice and the type of dice.
                                      For example, [(1, 8), (3, 4)] represents 1d8 and 3d4.
    
    Returns:
        Dict[str, Any]: A dictionary with the detailed results for each dice roll and the total.
    """
    detailed_results = []
    total = 0
    for num, die in dice:
        rolls = [random.randint(1, die) for _ in range(num)]
        detailed_results.append({
            "die": die,
            "num": num,
            "rolls": rolls
        })
        total += sum(rolls)
    return {"results": detailed_results, "total": total}