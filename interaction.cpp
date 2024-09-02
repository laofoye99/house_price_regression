/*This C++ file is used to create interaction terms in a dataframe.*/
#include <iostream>
#include <vector>

// Function to create interaction terms
std::vector<std::vector<int>> createInteractionTerms(const std::vector<std::vector<int>>& data) {
    std::vector<std::vector<int>> interactionTerms;

    // Iterate over each row in the data
    for (const auto& row : data) {
        std::vector<int> interactionRow;

        // Iterate over each column in the row
        for (size_t i = 0; i < row.size(); i++) {
            // Add the original value to the interaction row
            interactionRow.push_back(row[i]);

            // Create interaction terms by multiplying each pair of values
            for (size_t j = i + 1; j < row.size(); j++) {
                int interactionTerm = row[i] * row[j];
                interactionRow.push_back(interactionTerm);
            }
        }

        // Add the interaction row to the interaction terms
        interactionTerms.push_back(interactionRow);
    }

    return interactionTerms;
}

int main() {
    // Example usage
    std::vector<std::vector<int>> data = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    std::vector<std::vector<int>> interactionTerms = createInteractionTerms(data);

    // Print the interaction terms
    for (const auto& row : interactionTerms) {
        for (const auto& term : row) {
            std::cout << term << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
