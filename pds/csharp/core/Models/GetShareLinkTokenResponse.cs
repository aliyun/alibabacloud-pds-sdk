// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * get_share_token response
     */
    public class GetShareLinkTokenResponse : TeaModel {
        /// <summary>
        /// expire_time
        /// </summary>
        [NameInMap("expire_time")]
        [Validation(Required=true)]
        public string ExpireTime { get; set; }

        /// <summary>
        /// expires_in
        /// </summary>
        [NameInMap("expires_in")]
        [Validation(Required=true)]
        public long? ExpiresIn { get; set; }

        /// <summary>
        /// share_token
        /// </summary>
        [NameInMap("share_token")]
        [Validation(Required=true)]
        public string ShareToken { get; set; }

    }

}
