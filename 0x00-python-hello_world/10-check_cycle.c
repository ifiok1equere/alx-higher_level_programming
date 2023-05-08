#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *back, *front;

	back = list;
	front = list->next;
	while (front->next != NULL)
	{
		if (front->next == back || front->next == list)
			return (1);
		back = front;
		front = front->next;
	}
	return (0);
}
