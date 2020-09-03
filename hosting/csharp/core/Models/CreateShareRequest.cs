// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * create share request
     */
    public class CreateShareRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// description
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

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
        [Validation(Required=false)]
        public string Expiration { get; set; }

        /// <summary>
        /// creator
        /// </summary>
        [NameInMap("owner")]
        [Validation(Required=true)]
        public string Owner { get; set; }

        /// <summary>
        /// permissions
        /// </summary>
        [NameInMap("permissions")]
        [Validation(Required=false)]
        public List<string> Permissions { get; set; }

        /// <summary>
        /// share_file_path
        /// </summary>
        [NameInMap("share_file_path")]
        [Validation(Required=true)]
        public string ShareFilePath { get; set; }

        /// <summary>
        /// share_name
        /// </summary>
        [NameInMap("share_name")]
        [Validation(Required=false)]
        public string ShareName { get; set; }

        /// <summary>
        /// share create policy
        /// 
        /// share_policy
        /// </summary>
        [NameInMap("share_policy")]
        [Validation(Required=false)]
        public List<SharePermissionPolicy> SharePolicy { get; set; }

        /// <summary>
        /// status
        /// </summary>
        [NameInMap("status")]
        [Validation(Required=false)]
        public string Status { get; set; }

    }

}
