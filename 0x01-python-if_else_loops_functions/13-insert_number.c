#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_number - inserts a number into a sorted linked list
 * Description: inserts a number into a sorted linked list
 * @head: double pointer of the first node of linked list
 * @number: number of the node to inserted in linked list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *q;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}
	q = *head;
	while (q->next != NULL)
	{
		if (q->n > number)
		{
			node->next = q;
			*head = node;
			return (node);
		}
		if (q->next->n >= number)
		{
			node->next = q->next;
			q->next = node;
			return (node);
		}
		q = q->next;
	}
	node->next = NULL;
	return (node);
}
