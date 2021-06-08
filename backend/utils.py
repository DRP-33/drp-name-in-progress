#returns true if request_data contains all entries of required_data
def is_valid_request(request_data, required_data):
  for datum in required_data:
    if datum not in request_data:
      return False
  return True
