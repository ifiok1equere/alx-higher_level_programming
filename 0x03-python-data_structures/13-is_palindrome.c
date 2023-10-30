#include "lists.h"
/**
 * is_palindrome - function checks if a linked listis a palindrome
 * @head: pointer to the head node of the linked list
 * Return: return 1 for palindrome, 0 for ~palindrome
 */

int is_palindrome(listint_t **head)
{
	int i = 1, j, k = 0, l;
	listint_t *ptr_front = *head, *ptr_back = *head;

	if (*head == NULL)
		return (1);
	while (ptr_back->next != NULL)
	{
		i++;
		ptr_back = ptr_back->next;
	}
	l = i / 2;
	while (ptr_front->next != ptr_back && ptr_front != ptr_back)
	{
		if (ptr_front->n == ptr_back->n)
		{
			--i;
			ptr_back = *head;
			for (j = 1; j < i; j++)
				ptr_back = ptr_back->next;
			if (k <= l)
				ptr_front = ptr_front->next;
			k++;
		}
		else
			return (0);
	}
	if (ptr_front->n == ptr_back->n)
	{
		return (1);
	}
	return (0);
}
