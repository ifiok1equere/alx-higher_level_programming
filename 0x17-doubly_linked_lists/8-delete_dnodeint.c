#include "lists.h"
/**
 * delete_dnodeint_at_index - inserts a new node @ a position
 * @head: head pointer to the head node
 * @index: position where node is to be inserted
 * Return: address of the new node
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int i = 0, count = 0;
	dlistint_t *ptr = *head;

	if (*head == NULL)
		return (-1);
	if (index == 0)
	{
		if ((*head)->prev == NULL && (*head)->next ==  NULL)
		{
			*head = NULL;
			free(ptr);
			return (1);
		}
		else
		{
		(*head)->next->prev = NULL;
		*head = (*head)->next;
		ptr->next = NULL;
		free(ptr);
		return (1);
		}
	}
	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}
	if (index > count)
		return (-1);
	ptr = *head;
	while (i < index)
	{
		ptr = ptr->next;
		i++;
	}
	ptr->prev->next = ptr->next;
	ptr->next->prev = ptr->prev;
	free(ptr);
	return (1);
}
