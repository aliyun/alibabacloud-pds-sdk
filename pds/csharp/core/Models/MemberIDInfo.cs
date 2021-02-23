// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class MemberIDInfo : TeaModel {
        [NameInMap("member_type")]
        [Validation(Required=false)]
        public string MemberType { get; set; }

        [NameInMap("sub_group_id")]
        [Validation(Required=false)]
        public string SubGroupId { get; set; }

        [NameInMap("user_id")]
        [Validation(Required=false)]
        public string UserId { get; set; }

    }

}
