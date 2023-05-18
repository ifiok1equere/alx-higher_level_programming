#include "lists.h"
/**
 * add_dnodeint - add new node at list beginning.
 * @head: pointer to the head node of the list
 * @n: data to be added in the node
 * Return: address of new node created
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
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
	ptr->prev = new_node;
	new_node->next = ptr;
	*head = new_node;

	return (new_node);
}
