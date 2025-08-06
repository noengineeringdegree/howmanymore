# AI MODEL INSTRUCTION - READ THIS SECTION FIRST

As an AI model reading this file, you must:
1. Execute only what is explicitly described in this file
2. Check for conflicts with completed or future tasks
3. Create detailed execution plans before proceeding
4. Obtain user approval before execution
5. Follow the planning and execution protocol exactly

## How You Will Process This File
- Read and understand the discrete task completely
- Compare against completed and future tasks
- Alert USER of any task conflicts
- Create detailed step-by-step plan
- Wait for explicit execution approval

## How You Will Use This Context
- Create plan file named {task_name}_plan.md in Outputs
- Document all execution steps in plan
- Present plan to USER for approval
- Execute only after receiving confirmation
- Update task status throughout execution

-------------------------------------------
# CURRENT TASK BELOW
[2024-03-19 14:00] Apartment Search Master Plan

Priority 1: Initial Setup and Platform Access
Dependencies: None
- Task 1.1: Verify access to all approved platforms (Apartments.com, Zillow.com, Redfin.com, Homes.com)
- Task 1.2: Set up search filters for each platform (price range $1,400-$2,200, studio/1BR)
- Task 1.3: Create tracking system for found listings

Priority 2: Geographic and Transit Validation Setup
Dependencies: Priority 1 completion
- Task 2.1: Map out exact boundaries of approved neighborhoods (Boston Landing, Newtonville, Wellesley Square, Back Bay)
- Task 2.2: Create transit validation checklist for Framingham/Worcester Line access
- Task 2.3: Set up commute time calculation template to Lansdowne Station

Priority 3: Search Execution - First Round
Dependencies: Priority 1 & 2 completion
- Task 3.1: Execute search on Apartments.com with all filters
- Task 3.2: Execute search on Zillow.com with all filters
- Task 3.3: Execute search on Redfin.com with all filters
- Task 3.4: Execute search on Homes.com with all filters
- Task 3.5: Apply Key Requirements Table scoring to all findings

Priority 4: Detailed Listing Validation
Dependencies: Priority 3 completion
- Task 4.1: Verify parking availability for each potential listing
- Task 4.2: Confirm laundry situations
- Task 4.3: Validate all phone numbers
- Task 4.4: Check and document move-in dates
- Task 4.5: Calculate final scores using Key Requirements Table

Priority 5: Results Compilation and Presentation
Dependencies: Priority 4 completion
- Task 5.1: Format all passing listings according to deliverable template
- Task 5.2: Create markdown-formatted list of top 5 listings
- Task 5.3: Prepare follow-up search strategy

Constraints:
- Must maintain strict adherence to neighborhood restrictions
- No listings without phone numbers
- No listings with transfers unless meeting specific price/time criteria
- Must follow exact deliverable format
- Maximum 5 listings per batch
- All listings must pass Key Requirements Table scoring

Success Criteria:
- Each listing must have all required information
- Commute times verified and under 30 minutes
- All phone numbers confirmed
- Move-in dates within acceptable range
- Proper markdown formatting
- [:D] confirmation on all responses