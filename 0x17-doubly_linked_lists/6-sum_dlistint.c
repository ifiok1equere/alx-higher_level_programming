#include "lists.h"
/**
 * sum_dlistint - sums all data of a linkedlist.
 * @head: pointer to the head node of the list
 * Return: sum of all data of a linkedlist
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *ptr;
	int sum = 0;

	if (head == NULL)
		return (0);
	ptr = head;
	while (ptr != NULL)
	{
		sum += ptr->n;
		ptr = ptr->next;
	}

	return (sum);
}
