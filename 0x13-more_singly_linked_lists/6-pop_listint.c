#include "lists.h"
/**
 * pop_listint -  this function deletes the head
 * node of a listint_t linked list, and returns
 * the head node’s data (n).
 * @head: this is a pointer to de first node
 * Return: the head node’s data (n) or 0 if head is iqual a NULL.
 */
int pop_listint(listint_t **head)
{
	listint_t *temp;
	int n;

	if (head == NULL || *head == NULL)
	return (0);
	n = (*head)->n;
	temp = *head;
	*head = (*head)->next;
	free(temp);
	return (n);
}
