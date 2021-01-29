// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * create_share_link response
     */
    public class CreateShareLinkResponse : TeaModel {
        /// <summary>
        /// description
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false)]
        public string ShareId { get; set; }

        /// <summary>
        /// share_msg
        /// </summary>
        [NameInMap("share_msg")]
        [Validation(Required=false)]
        public string ShareMsg { get; set; }

        /// <summary>
        /// share_name
        /// </summary>
        [NameInMap("share_name")]
        [Validation(Required=false)]
        public string ShareName { get; set; }

        /// <summary>
        /// share_policy
        /// </summary>
        [NameInMap("share_policy")]
        [Validation(Required=false)]
        public string SharePolicy { get; set; }

        /// <summary>
        /// share_pwd
        /// </summary>
        [NameInMap("share_pwd")]
        [Validation(Required=false)]
        public string SharePwd { get; set; }

        /// <summary>
        /// share_url
        /// </summary>
        [NameInMap("share_url")]
        [Validation(Required=false)]
        public string ShareUrl { get; set; }

    }

}
