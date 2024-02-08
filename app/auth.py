# # from functools import wraps
# # from flask import request,jsonify

# # from app.schema.schema import User
# # from flask_jwt_extended import decode_token 


# # def custom_token_required(f):     
# #         @wraps(f)
# #         def decorator(*args, **kwargs):
# #             print("aaaaaaaaaaaaaaaaaaaaaaaahhhhha")
# #             token = None
# #             # ensure the jwt-token is passed with the headers
# #             if 'x-access-token' in request.headers:
# #                 token = request.headers['x-access-token']
# #             if not token: # throw error if no token provided
# #                 return jsonify({"message": "A valid token is missing!"}),401
# #             try:
# #                 print("bccbcnnccncvcvddvcn")
# #             # decode the token to obtain user public_id
                
                

# #                 current_user = User.get(user_id=data['user_id']).first()
# #             except:
# #                 print("nbnbbb")
# #                 return jsonify({"message": "Invalid token!"}), 401
# #             # Return the user information attached to the token
# #             return f(" ", *args, **kwargs)
# #         return decorator

#  # auth.py

# # from functools import wraps
# # from flask import request, jsonify
# # from flask_jwt_extended import decode_token
# # from flask_login import current_user
# # from app.schema.schema import User

# # def custom_token_required(f):
# #     @wraps(f)
# #     def decorator(*args, **kwargs):
# #         print("aaaaaaaaaaaaaaaaaaaaaaaahhhhha")
# #         token = None
# #         # Ensure the jwt-token is passed with the headers
# #         if 'x-access-token' in request.headers:
# #             token = request.headers['x-access-token']
# #         if not token: # Throw an error if no token provided
# #             return jsonify({"message": "A valid token is missing!"}), 401
# #         try:
# #             # Decode the token to obtain user public_id
# #             data = decode_token(token)
# #             print("Decoded Token Data:", data)

# #             # Extract user_id from the decoded token
# #             user_id = data['identity']

# #             # Check if the current_user is authenticated
# #             if not current_user.is_authenticated:
# #                 raise Exception("User not authenticated.")

# #             # Check if the current_user id matches the user_id from the token
# #             if str(current_user.id) != str(user_id):
# #                 raise Exception("Token user_id does not match current_user id.")

# #             # Continue with the original function
# #             return f(*args, **kwargs)

# #         except Exception as e:
# #             print("Error decoding or fetching user:", str(e))
# #             return jsonify({"message": "Invalid token!"}), 401

# #     return decorator

# from functools import wraps
# from flask import request, jsonify
# from app.schema.schema import User
# from flask_jwt_extended import create_access_token, decode_token

# def custom_token_required(f):     
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         print("aaaaaaaaaaaaaaaaaaaaaaaahhhhha")
#         token = None
#         # Ensure the jwt-token is passed with the headers
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#         if not token: # Throw an error if no token provided
#             return jsonify({"message": "A valid token is missing!"}), 401
#         try:
#             # Decode the token to obtain user public_id
#             data = decode_token(token)
#             print("Decoded Token Data:", data)

#             # Fetch the user from the database using user_id from the token
#             user = User.get(user_id=data['user_id'])
#             if user:
#                 print("ggggggggggggggggggg")
#                 # Attach the user to the current request context
#                 kwargs['current_user'] = user
#             else:
#                 raise Exception("User not found in the database.")

#         except Exception as e:
#             print("Error decoding or fetching user:", str(e))
#             return jsonify({"message": "Invalid token!"}), 401

#         # Continue with the original function
#         return f(*args, **kwargs)

#     return decorator




