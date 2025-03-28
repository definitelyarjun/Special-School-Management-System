from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud.user import user
from app.schemas.user import UserCreate
from app.models.user import UserRole
import argparse

def setup_admin() -> None:
    """Ensure an admin user exists with the correct role."""
    db = SessionLocal()
    try:
        # Check if admin user already exists
        admin = user.get_by_username(db, username="admin")
        
        if admin:
            print("Admin user exists")
            
            # Check if the role needs to be fixed
            if admin.role != UserRole.ADMIN:
                print(f"Updating role from {admin.role} to {UserRole.ADMIN}")
                admin.role = UserRole.ADMIN
                admin.is_superuser = True
                db.commit()
                db.refresh(admin)
                print("Admin role updated successfully")
            else:
                print("Admin role is already correct")
        else:
            # Create admin user
            print("Creating new admin user")
            admin_in = UserCreate(
                username="admin",
                email="admin@example.com",
                password="admin123",  # Change this to a secure password
                is_superuser=True,
                is_active=True,
                role=UserRole.ADMIN
            )
            user.create(db, obj_in=admin_in)
            print("Admin user created successfully")
    finally:
        db.close()

def check_role() -> None:
    """Check the current role of the admin user."""
    db = SessionLocal()
    try:
        # Get the admin user
        admin = user.get_by_username(db, username="admin")
        if admin:
            print(f"Admin user exists with role: {admin.role}")
            print(f"Role type: {type(admin.role)}")
            print(f"Is superuser: {admin.is_superuser}")
        else:
            print("Admin user does not exist")
    finally:
        db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Admin user management utilities")
    parser.add_argument("action", choices=["setup", "check"], 
                        help="Action to perform: setup (ensure admin exists with correct role) or check")
    
    args = parser.parse_args()
    
    if args.action == "setup":
        setup_admin()
    elif args.action == "check":
        check_role() 