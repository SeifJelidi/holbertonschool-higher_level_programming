#include <unistd.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * Description: checks if a singly linked list has a cycle in it
 * @head: pointer to head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *head)
{
	listint_t *q1, *q2;

	if (head == NULL)
		return (0);
	q1 = head;
	q2 = head;
	while (q1 && q2 && q2->next)
	{
		q1 = q1->next;
		q2 = q2->next->next;
		if (q1 == q2)
			return (1);
	}
	return (0);
}
