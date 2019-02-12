from typing import List, Union

CSVHeader = List[Union[str, 'CSVHeader']]

# Eight CSV header
eightheader: CSVHeader = \
    ['会社名', '部署名', '役職', '氏名', 'e-mail', '郵便番号', '住所', 'TEL会社', 'TEL部門', 'TEL直通',
        'Fax', '携帯電話', 'URL', '名刺交換日', 'Eightでつながっている人', '再データ化中の名刺', '\'?\'を含んだデータ']

# Google Contact header
gcheader: CSVHeader = \
    ['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 
        'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 'Name Suffix',
        'Initials', 'Nickname', 'Short Name', 'Maiden Name', 'Birthday', 'Gender', 'Location', 
        'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity', 
        'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership', 'E-mail 1 - Type',
        'E-mail 1 - Value', 'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type', 'Phone 2 - Value',
        'Phone 3 - Type', 'Phone 3 - Value', 'Address 1 - Type',
        'Address 1 - Formatted', 'Address 1 - Street', 'Address 1 - City',
        'Address 1 - PO Box', 'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country',
        'Address 1 - Extended Address', 'Address 2 - Type', 'Address 2 - Formatted', 'Address 2 - Street',
        'Address 2 - City', 'Address 2 - PO Box', 'Address 2 - Region', 'Address 2 - Postal Code',
        'Address 2 - Country', 'Address 2 - Extended Address', 'Organization 1 - Type',
        'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title',
        'Organization 1 - Department', 'Organization 1 - Symbol', 'Organization 1 - Location',
        'Organization 1 - Job Description', 'Website 1 - Type', 'Website 1 - Value']

