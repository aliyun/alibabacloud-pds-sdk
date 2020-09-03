// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * Update share response
     */
    public class UpdateShareResponse : TeaModel {
        /// <summary>
        /// created_at
        /// </summary>
        [NameInMap("created_at")]
        [Validation(Required=false)]
        public string CreatedAt { get; set; }

        /// <summary>
        /// creator
        /// </summary>
        [NameInMap("creator")]
        [Validation(Required=false)]
        public string Creator { get; set; }

        /// <summary>
        /// description
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

        /// <summary>
        /// domain_id
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=false)]
        public string DomainId { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false)]
        public string DriveId { get; set; }

        /// <summary>
        /// expiration
        /// </summary>
        [NameInMap("expiration")]
        [Validation(Required=false)]
        public string Expiration { get; set; }

        /// <summary>
        /// expired
        /// </summary>
        [NameInMap("expired")]
        [Validation(Required=false)]
        public bool? Expired { get; set; }

        /// <summary>
        /// owner
        /// </summary>
        [NameInMap("owner")]
        [Validation(Required=false)]
        public string Owner { get; set; }

        /// <summary>
        /// permissions
        /// </summary>
        [NameInMap("permissions")]
        [Validation(Required=false)]
        public List<string> Permissions { get; set; }

        /// <summary>
        /// share_path
        /// </summary>
        [NameInMap("share_file_path")]
        [Validation(Required=false)]
        public string ShareFilePath { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false)]
        public string ShareId { get; set; }

        /// <summary>
        /// share_name
        /// </summary>
        [NameInMap("share_name")]
        [Validation(Required=false)]
        public string ShareName { get; set; }

        [NameInMap("share_policy")]
        [Validation(Required=false)]
        public List<SharePermissionPolicy> SharePolicy { get; set; }

        /// <summary>
        /// status
        /// </summary>
        [NameInMap("status")]
        [Validation(Required=false)]
        public string Status { get; set; }

        /// <summary>
        /// updated_at
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=false)]
        public string UpdatedAt { get; set; }

    }

}
