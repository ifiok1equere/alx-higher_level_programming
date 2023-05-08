#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *front, *back;

	if (list == NULL)
		return (0);

	back = list;
	front = list->next;

	while (front != NULL)
	{
		if (front->next == list || front->next == back)
			return (1);
		back = front;
		front = front->next;
	}
	return (0);
}
