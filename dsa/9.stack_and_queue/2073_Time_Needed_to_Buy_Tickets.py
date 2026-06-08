import typing as t

class Solution:
    def timeRequiredToBuy(self, tickets: t.List[int], k: int) -> int:
        num_of_ticket: int = tickets[k]
        result: int = 0
        for ind in range(0, len(tickets), 1):
            if ind < k:
                result += (
                    tickets[ind] 
                    if tickets[ind] < num_of_ticket 
                    else num_of_ticket
                )
            elif ind > k:
                result += (
                    tickets[ind]
                    if tickets[ind] < num_of_ticket
                    else num_of_ticket - 1
                )
            else:
                result += num_of_ticket
        
        return result