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
    public class ActorAliUser : TeaModel {
        /// <summary>
        /// AliUserID
        /// </summary>
        [NameInMap("ali_user_id")]
        [Validation(Required=false)]
        public string AliUserId { get; set; }

        /// <summary>
        /// AliUserType
        /// </summary>
        [NameInMap("ali_user_type")]
        [Validation(Required=false)]
        public string AliUserType { get; set; }

    }

}
