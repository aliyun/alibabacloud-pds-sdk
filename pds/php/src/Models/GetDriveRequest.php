<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Get drive request.
 */
class GetDriveRequest extends Model
{
    public $headers;

    /**
     * @description Drive ID
     *
     * @example 123
     *
     * @var string
     */
    public $driveId;

    /**
     * @description Subdomain ID
     *
     * @example hz-123
     *
     * @var string
     */
    public $subdomainId;
    protected $_name = [
        'driveId'     => 'drive_id',
        'subdomainId' => 'subdomain_id',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetDriveRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }

        return $model;
    }
}
