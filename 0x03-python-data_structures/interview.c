#include "lists.h"
/**
 * is_palindrome - function checks if a linked listis a palindrome
 * @head: pointer to the head node of the linked list
 * Return: return 1 for success, 0 for failure
 */

int is_palindrome(listint_t **head)
{
	int i = 1, j, k = 0, l;
	listint_t *ptr_front = *head;
	listint_t *ptr_back = *head;

	if (*head == NULL)
		return (1);
	while (ptr_back->next != NULL)
	{
		i++;
		ptr_back = ptr_back->next;
	}
	l = i / 2;
	/*printf("At start: front: %d, back: %d\n", ptr_front->n,
	 * ptr_back->n);*/
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
			/*printf("front: %d, back: %d\n", ptr_front->n, ptr_back->n);*/
			/*printf("And counter i is: %d\n", i);*/
		}
		else
		{
			return (0);
		}
	}
	if (ptr_front->n == ptr_back->n)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
