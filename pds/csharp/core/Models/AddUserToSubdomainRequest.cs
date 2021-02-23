// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * Add user to subdomain request
     */
    public class AddUserToSubdomainRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// subdomain id
        /// </summary>
        [NameInMap("subdomain_id")]
        [Validation(Required=false)]
        public string SubdomainId { get; set; }

        /// <summary>
        /// 用户 ID
        /// </summary>
        [NameInMap("user_id")]
        [Validation(Required=true)]
        public string UserId { get; set; }

    }

}
