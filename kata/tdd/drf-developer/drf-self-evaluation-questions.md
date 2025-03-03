## Django Rest Framework Engineer - Questions for Self Evaluation

### Introduction to Django Rest Framework

1. What is Django Rest Framework (DRF)?
2. How does DRF integrate with Django?
3. Why would you use DRF over Django's built-in views?
4. What are the key features of DRF?
5. What is the role of serializers in DRF?

### Installation and Setup

6. How do you install DRF in a Django project?
7. What are the basic settings required to configure DRF?
8. How do you add DRF to the installed apps in a Django project?
9. What middleware is necessary for DRF?

### Serializers

10. What is a serializer in DRF?
11. How do serializers differ from Django forms?
12. How do you create a simple serializer?
13. What is the purpose of the `Meta` class in a serializer?
14. How do you validate data in a serializer?
15. What methods can be overridden in a serializer for custom behavior?
16. How can you handle nested serializers?
17. What is the difference between `Serializer` and `ModelSerializer`?

### Views and ViewSets

18. What is a ViewSet in DRF?
19. How does a ViewSet differ from a standard Django view?
20. What are the advantages of using ViewSets?
21. What is the purpose of the `@action` decorator in a ViewSet?
22. How do you create a read-only ViewSet?
23. How do you override default methods in a ViewSet?
24. What is the difference between `APIView` and `GenericAPIView`?

### Routers

25. What is a router in DRF?
26. How do routers simplify URL configuration in DRF?
27. How do you register a ViewSet with a router?
28. What is the difference between `SimpleRouter` and `DefaultRouter`?

### Authentication and Permissions

29. What authentication classes are provided by DRF?
30. How do you set up token-based authentication in DRF?
31. What are the common permission classes in DRF?
32. How do you apply custom permissions to a ViewSet or APIView?
33. How does DRF handle user authentication in the request cycle?
34. What is the purpose of the `IsAuthenticated` permission class?

### Throttling

35. What is throttling in DRF?
36. How do you set up throttling for an API endpoint?
37. What are the different types of throttles provided by DRF?
38. How do you implement custom throttling?

### Pagination

39. What is pagination in DRF?
40. How do you configure pagination globally for a DRF project?
41. What are the different pagination styles available in DRF?
42. How do you apply pagination to a specific ViewSet or APIView?

### Filtering, Searching, and Ordering

43. How do you implement filtering in DRF?
44. What is the purpose of the `django-filter` package in DRF?
45. How do you enable searching in a DRF ViewSet?
46. How do you implement ordering in DRF?

### Testing

47. How do you test DRF views?
48. What is the purpose of `APITestCase` in DRF?
49. How do you use the `APIClient` for testing in DRF?
50. How do you test authentication in DRF?

### Nested and Related Resources

51. How do you handle nested resources in DRF?
52. What are the ways to represent relationships in DRF serializers?
53. How do you use `HyperlinkedModelSerializer`?

### Performance and Optimization

54. How can you optimize query performance in DRF?
55. What are the benefits of using `select_related` and `prefetch_related`?
56. How do you cache API responses in DRF?

### Advanced Topics (Optional)

57. How do you create a custom renderer in DRF?
58. What is the purpose of a parser in DRF?
59. How do you implement a custom permission class?
60. How do you handle file uploads in DRF?
61. How do you customize error handling in DRF?

### Deployment and Security

62. What are the best practices for deploying a DRF application?
63. How do you secure sensitive data in DRF?
64. How do you handle CORS in DRF?

### Real-world Scenarios

65. How would you implement rate limiting for a public API?
66. How can you manage versioning in DRF?
67. How do you handle large datasets with DRF?

### JSON Web Tokens (JWT)

68. How do you implement JWT authentication in DRF?
69. What are the benefits of using JWT over token authentication?
70. How do you refresh tokens in a JWT setup?


### Django Models

1. How would you test if a record with given primary key value exists?
   1. try Model.objects.get(pk=pk)
   2. Model.objects.filter(pk=pk).exists()

