#include "lists.h"
/**
 * free_dlistint - frees a doubly linked list.
 * @head: pointer to the head node of the list
 * Return: void
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *ptr;

	if (head == NULL)
	{
		return;
	}
	ptr = head;
	while (head != NULL)
	{
		head = head->next;
		free(ptr);
		/* free(ptr); */
		ptr = head;
	}
}

