#include "lists.h"
/**
 * add_dnodeint_end - add new node at list end.
 * @head: pointer to the head node of the list
 * @n: data to be added in the node
 * Return: address of new node created
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node, *ptr;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	ptr = *head;
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	ptr->next = new_node;
	new_node->prev = ptr;

	return (new_node);
}
