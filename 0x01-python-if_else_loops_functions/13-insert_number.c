#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a new node in a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be inserted in sorted order in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *previous;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->n < number)
			{
				previous = current;
				current = current->next;
			}
			else
			{
				new->next = current;
				previous->next = new;
				break;
			}
		}
	}

	return (new);
}
