#include "lists.h"
/**
 * insert_dnodeint_at_index - inserts a new node @ a position
 * @h: head pointer to the head node
 * @idx: position where node is to be inserted
 * @n: data to be inerted into node
 * Return: address of the new node
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	unsigned int i = 0, count = 0;
	dlistint_t *new_node, *ptr = *h;

	if (idx == 0)
	{
		new_node = add_dnodeint(h, n);
		return (new_node);
	}
	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}
	if (idx > count)
		return (NULL);
	ptr = *h;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = NULL;

	while (i < idx - 1)
	{
		ptr = ptr->next;
		i++;
	}
	new_node->next = ptr->next;
	new_node->prev = ptr;
	ptr->next->prev = new_node;
	ptr->next = new_node;

	return (new_node);
}
