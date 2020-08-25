// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * get_share_id request
     */
    public class GetShareLinkIDRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// share_msg
        /// </summary>
        [NameInMap("share_msg")]
        [Validation(Required=false)]
        public string ShareMsg { get; set; }

    }

}
