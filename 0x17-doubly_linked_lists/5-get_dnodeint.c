#include "lists.h"
/**
 * get_dnodeint_at_index - searches for the nth node of a list.
 * @head: pointer to the head node of the list
 * @index: position of node to be returned
 * Return: nth node of a list
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *ptr;
	unsigned int i = 0;

	if (head == NULL)
	{
		return (NULL);
	}
	ptr = head;
	while (i < index)
	{
		ptr = ptr->next;
		i++;
	}

	return (ptr);
}
