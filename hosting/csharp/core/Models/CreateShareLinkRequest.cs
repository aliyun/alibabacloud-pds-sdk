// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * create_share_link request
     */
    public class CreateShareLinkRequest : TeaModel {
        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// expiration
        /// </summary>
        [NameInMap("expiration")]
        [Validation(Required=true)]
        public string Expiration { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=true)]
        public string FileId { get; set; }

        /// <summary>
        /// share_pwd
        /// </summary>
        [NameInMap("share_pwd")]
        [Validation(Required=false)]
        public string SharePwd { get; set; }

    }

}
