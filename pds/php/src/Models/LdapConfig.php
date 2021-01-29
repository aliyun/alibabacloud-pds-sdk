<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class LdapConfig extends Model {
    protected $_name = [
        'adminDn' => 'admin_dn',
        'adminPassword' => 'admin_password',
        'baseDn' => 'base_dn',
        'host' => 'host',
        'port' => 'port',
        'uid' => 'uid',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->adminDn) {
            $res['admin_dn'] = $this->adminDn;
        }
        if (null !== $this->adminPassword) {
            $res['admin_password'] = $this->adminPassword;
        }
        if (null !== $this->baseDn) {
            $res['base_dn'] = $this->baseDn;
        }
        if (null !== $this->host) {
            $res['host'] = $this->host;
        }
        if (null !== $this->port) {
            $res['port'] = $this->port;
        }
        if (null !== $this->uid) {
            $res['uid'] = $this->uid;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return LdapConfig
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['admin_dn'])){
            $model->adminDn = $map['admin_dn'];
        }
        if(isset($map['admin_password'])){
            $model->adminPassword = $map['admin_password'];
        }
        if(isset($map['base_dn'])){
            $model->baseDn = $map['base_dn'];
        }
        if(isset($map['host'])){
            $model->host = $map['host'];
        }
        if(isset($map['port'])){
            $model->port = $map['port'];
        }
        if(isset($map['uid'])){
            $model->uid = $map['uid'];
        }
        return $model;
    }
    /**
     * @var string
     */
    public $adminDn;

    /**
     * @var string
     */
    public $adminPassword;

    /**
     * @var string
     */
    public $baseDn;

    /**
     * @var string
     */
    public $host;

    /**
     * @var int
     */
    public $port;

    /**
     * @var string
     */
    public $uid;

}
