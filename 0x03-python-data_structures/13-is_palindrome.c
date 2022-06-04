#include "lists.h"
listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_listint - Reverses a singly linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *nod = *head, *nxt, *prev = NULL;
while (nod)
{
nxt = nod->nxt;
nod->nxt = prev;
prev = nod;
nod = nxt;
}
*head = prev;
return (*head);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If it is - 0.
 *         If not - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *tp, *rvs, *md;
size_t sz = 0, a;
if (*head == NULL || (*head)->nxt == NULL)
return (1);
tp = *head;
while (tp)
{
sz++;
tp = tp->nxt;
}
tp = *head;
for (a = 0; a < (sz / 2) - 1; a++)
tp = tp->nxt;
if ((sz % 2) == 0 && tp->n != tp->nxt->n)
return (0);
tp = tp->nxt->nxt;
rvs = reverse_listint(&tp);
md = rvs;
tp = *head;
while (rvs)
{
if (tp->n != rvs->n)
return (0);
tp = tp->nxt;
rvs = rvs->nxt;
}
reverse_listint(&md);
return (1);
}
