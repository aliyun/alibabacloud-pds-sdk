<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class SetBizCNameCertRequest extends Model
{
    /**
     * @var string
     */
    public $CertID;

    /**
     * @description biz cname
     *
     * @example api.yoursite.com
     *
     * @var string
     */
    public $bizCname;

    /**
     * @description cert body
     *
     * @example xxxxxxxxxxx
     *
     * @var string
     */
    public $certBody;

    /**
     * @description cert name
     *
     * @example mysite2020cert
     *
     * @var string
     */
    public $certName;

    /**
     * @description cert privatekey
     *
     * @example yyyyyyyyyy
     *
     * @var string
     */
    public $certPrivatekey;

    /**
     * @description cname type
     *
     * @example auth
     *
     * @var string
     */
    public $cnameType;

    /**
     * @description domain ID
     *
     * @example sz100
     *
     * @var string
     */
    public $domainId;

    /**
     * @description biz cname
     *
     * @example true
     *
     * @var bool
     */
    public $isVpc;
    protected $_name = [
        'CertID'         => 'CertID',
        'bizCname'       => 'biz_cname',
        'certBody'       => 'cert_body',
        'certName'       => 'cert_name',
        'certPrivatekey' => 'cert_privatekey',
        'cnameType'      => 'cname_type',
        'domainId'       => 'domain_id',
        'isVpc'          => 'is_vpc',
    ];

    public function validate()
    {
        Model::validateRequired('certBody', $this->certBody, true);
        Model::validateRequired('certName', $this->certName, true);
        Model::validateRequired('certPrivatekey', $this->certPrivatekey, true);
        Model::validateRequired('cnameType', $this->cnameType, true);
        Model::validateRequired('domainId', $this->domainId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->CertID) {
            $res['CertID'] = $this->CertID;
        }
        if (null !== $this->bizCname) {
            $res['biz_cname'] = $this->bizCname;
        }
        if (null !== $this->certBody) {
            $res['cert_body'] = $this->certBody;
        }
        if (null !== $this->certName) {
            $res['cert_name'] = $this->certName;
        }
        if (null !== $this->certPrivatekey) {
            $res['cert_privatekey'] = $this->certPrivatekey;
        }
        if (null !== $this->cnameType) {
            $res['cname_type'] = $this->cnameType;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->isVpc) {
            $res['is_vpc'] = $this->isVpc;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return SetBizCNameCertRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['CertID'])) {
            $model->CertID = $map['CertID'];
        }
        if (isset($map['biz_cname'])) {
            $model->bizCname = $map['biz_cname'];
        }
        if (isset($map['cert_body'])) {
            $model->certBody = $map['cert_body'];
        }
        if (isset($map['cert_name'])) {
            $model->certName = $map['cert_name'];
        }
        if (isset($map['cert_privatekey'])) {
            $model->certPrivatekey = $map['cert_privatekey'];
        }
        if (isset($map['cname_type'])) {
            $model->cnameType = $map['cname_type'];
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }
        if (isset($map['is_vpc'])) {
            $model->isVpc = $map['is_vpc'];
        }

        return $model;
    }
}
