#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *front;

	if (list == NULL)
		return (0);

	front = list->next;

	while (front != NULL)
	{
		if (front->next == list)
			return (1);
		front = front->next;
	}
	return (0);
}
